from .models import CartItem

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        item_count = cart_items.count()
    else:
        item_count = 0
    return {'cart_item_count': item_count}
