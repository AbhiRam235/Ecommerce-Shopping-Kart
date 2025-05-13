from .models import Cart, CartItem
from .views import _cart_id
from django.db.models import Sum

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = None

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    elif cart:
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        cart_items = []

    # Safe sum using loop
    for cart_item in cart_items:
        cart_count += cart_item.quantity

    return dict(cart_count=cart_count)
