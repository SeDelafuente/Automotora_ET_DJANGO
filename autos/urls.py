from django.urls import path
from .views import index, car_list, car_detail, cart, add_to_cart, remove_from_cart, remove_item_from_cart, checkout, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('cars/', car_list, name='car_list'),
    path('cars/<int:car_id>/', car_detail, name='car_detail'),
    path('cart/', cart, name='cart'),
    path('add_to_cart/<int:car_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:car_id>/', remove_from_cart, name='remove_from_cart'),
    path('remove_item_from_cart/<int:car_id>/', remove_item_from_cart, name='remove_item_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
