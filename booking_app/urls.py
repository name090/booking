from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('apartment/<int:apartment_id>/', views.booking, name='booking_page'),
]