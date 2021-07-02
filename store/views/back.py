
from django.shortcuts import redirect
from django.views import View

class Store(View):

    def get(self, request):
        return redirect('homepage')

