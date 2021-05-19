from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51InnIvFl4lG8CSXrigliIUwiucMHa84VL56Mb6hdz0i1kfzB1caCiAB1Zf6gz2HeeI92cE6i8wKc3034MKlfGTTC00V0iYs0mq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
