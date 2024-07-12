from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Car, CartItem

def index(request):
    return render(request, 'autos/index.html')

def car_list(request):
    cars = Car.objects.all()
    cart_item_count = CartItem.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    context = {
        'cars': cars,
        'cart_item_count': cart_item_count,
    }
    return render(request, 'autos/car_list.html', context)

@login_required
def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, car=car)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('car_list')

@login_required
def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total = sum(item.car.price * item.quantity for item in cart_items)
    total_quantity = sum(item.quantity for item in cart_items)
    return render(request, 'autos/cart.html', {'cart_items': cart_items, 'total': total, 'total_quantity': total_quantity})

@login_required
def remove_from_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart_item = get_object_or_404(CartItem, user=request.user, car=car)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

@login_required
def remove_item_from_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart_item = get_object_or_404(CartItem, user=request.user, car=car)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, 'Compra realizada con éxito')
    return redirect('index')

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {
        'car': car,
    }
    return render(request, 'autos/car_detail.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
