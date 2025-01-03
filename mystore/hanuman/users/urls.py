from django.urls import path
from . import views
#from .views import prices
urlpatterns=[
    path(' ',views.all_user)
    #path('prices/',show_prices,name='prices')
]
