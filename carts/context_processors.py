from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # returns a single object
    except Cart.DoesNotExist:
        cart = None

    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            cart_count += item.quantity
    else:
        cart_count = 0

    return dict(cart_count=cart_count)
      