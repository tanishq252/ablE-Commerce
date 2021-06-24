from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        customer = Customer(first_name=first_name, last_name=last_name, password=password, phone=phone, email=email)

        # validation

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        error_m = self.validateCustomer(customer)

        if (not error_m):
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_m,
                'values': values,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_m = None

        if (not customer.first_name):
            error_m = "Please enter the first name for registration"
        elif len(customer.first_name) < 2:
            error_m = "First name must be more than 2 letters"
        elif (not customer.last_name):
            error_m = "Please enter the last name for registration"
        elif (not customer.phone):
            error_m = "Please enter the phone number for registration"
        elif (not customer.password):
            error_m = "Please enter the password for registration"
        elif len(customer.email) < 4:
            error_m = "INVALID MAIL ADDRESS"
        elif len(customer.last_name) < 2:
            error_m = "Last name must be more than 2 letters"
        elif len(customer.phone) < 10:
            error_m = "Phone number must be 10 digits"
        elif len(customer.password) < 8:
            error_m = "Password must be more than 8 letters"
        elif customer.isExists():
            error_m = "Email already exists by some other user"

        return error_m
