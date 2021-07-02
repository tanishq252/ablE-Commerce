
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render,redirect


class Login(View):

    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error = None
        if customer:
            fu = check_password(password, customer.password)
            if fu:
                request.session['customer'] = customer.id

                return redirect('homepage')
            else:
                error = 'INVALID EMAIL OR PASSWORD'

        else:
            error = 'INVALID EMAIL OR PASSWORD'
        print(customer)
        return render(request, 'login.html', {'error': error})


def logout(request):
    request.session.clear()
    return redirect('login')