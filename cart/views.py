from django.shortcuts import render, redirect, reverse, HttpResponse

def show_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    print(f"REQUEST: {request.POST}")

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


#https://stackoverflow.com/questions/60859234/remove-an-unique-item-from-shopping-cart-in-django
def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})


    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('show_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)