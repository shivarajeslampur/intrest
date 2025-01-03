from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('cart', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:item_id>', views.update_quantity, name='update_quantity'),
    path('bookNow', views.bookNow, name='bookNow'),
    #############################################################################################
      # Add trailing slash and name the URL pattern
]
