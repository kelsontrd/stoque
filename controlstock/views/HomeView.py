from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from controlstock.models.Product import Product

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        produtos = Product.objects.all()
        return render(request, 'home.html', {'produtos': produtos})
