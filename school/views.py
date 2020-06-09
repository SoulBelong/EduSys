from django.shortcuts import render,HttpResponse
from django import views

def show(req):
    return render(req,'login.html')

class Login(views.View):
    def get(self):
        return HttpResponse('ok')