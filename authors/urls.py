from django.urls import path
from . import views




urlpatterns = [
    path('', views.AuthorListCreateView.as_view()),
    path('<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view()),
]

     
