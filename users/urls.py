from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    LogoutView,
    
    FavoriteListView,
    FavoriteCreateView,
    FavoriteDeleteView,
    FavoriteDetailView,
    FavoriteToggleView,
    ClearAllFavoritesView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/add/', FavoriteCreateView.as_view(), name='favorite-add'),
    path('favorites/<int:pk>/', FavoriteDetailView.as_view(), name='favorite-detail'),
    path('favorites/<int:pk>/delete/', FavoriteDeleteView.as_view(), name='favorite-delete'),
    path('favorites/toggle/<int:book_id>/', FavoriteToggleView.as_view(), name='favorite-toggle'),
    path('favorites/clear-all/', ClearAllFavoritesView.as_view(), name='favorites-clear'),
]