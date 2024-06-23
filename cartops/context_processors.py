from .cart import Cart
#Create a context processor so that our cart is accessible from all pages

def cart_ctx(request):
    return {'mycart':Cart(request)} #create a cart object by passing the request