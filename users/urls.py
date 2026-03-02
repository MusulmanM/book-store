from django.urls import path
from .views import (Userapiview, Favoriteapiview)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('user/<int:pk>', Userapiview.as_view()),
    path('user/', Userapiview.as_view()),
    path('favorites/', Favoriteapiview.as_view()),
    path('favorite/<int:pk>', Favoriteapiview.as_view()),

]