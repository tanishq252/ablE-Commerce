from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.orders import Order

class Check(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        for p in products:
            print(cart.get(str(p.id)))
            order = Order(customer=Customer(id=customer),
                          product = p,
                          price = p.price,
                          address = address,
                          phone = phone,
                          q = cart.get(str(p.id))
                          )

            order.save()

            request.session['cart'] = {}

            order.placeOrder()

        return redirect('cart')
