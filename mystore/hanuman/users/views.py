from django.shortcuts import render
from django.http import HttpResponse
#from .models import product

# Create your views here.
def all_user(request):
    
    return HttpResponse('returning all users')



'''def show_prices(request):
    products = AgricultureProduct.objects.all()
    return render(request, 'prices.html', {'products': products})'''