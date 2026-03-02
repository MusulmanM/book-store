from django.urls import path
from .views import CartItemapiview, CartapiView

urlpatterns = [
    path('cart', CartapiView.as_view()),
    path('cartitem', CartItemapiview.as_view()),
    
]