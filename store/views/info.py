from store.models.info import Info
from django.shortcuts import render, redirect
from django.views import View


class Inf(View):

    def get(self,request):
        information = Info.info_get_all()
        return render(request, "info.html", {'information': information})
