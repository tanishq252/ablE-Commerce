from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.profile import Profile


class Profile_c(View):
    def post(self, request):
        customer = request.session.get('customer')
        pro = Profile.get_profile_customer(customer)
        print(pro)
        return render(request, 'base.html', {'pro': pro})
