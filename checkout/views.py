from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QFedvHPsg9Sgnt3FcuyqeE1Xo9zTFza2rXecnhlDZQFDQ0H7GHW91kU8swtyL5nKekF37D6THK8n7W5zzu3CKJy00AMuNw6F0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)