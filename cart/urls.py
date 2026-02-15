from django.urls import path
from .views import (
    CartDetailView,
    CartItemCreateView,
    CartItemUpdateView,
    CartItemDeleteView,
    CartClearView,
    CartItemQuantityView
)

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),
    path('clear/', CartClearView.as_view(), name='cart-clear'),
    path('add/', CartItemCreateView.as_view(), name='cart-add'),
    path('item/<int:pk>/', CartItemUpdateView.as_view(), name='cart-item-update'),
    path('item/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-item-delete'),
    path('item/<int:item_id>/<str:action>/', CartItemQuantityView.as_view(), name='cart-item-quantity'),
]