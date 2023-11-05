"""
URL configuration for HBMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views

from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include

from . import views
urlpatterns = [

    path('', views.home, name="home"),
    path('register/', views.register, name="register"),


    path('login/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name='login'),
    path('send_otp/', views.send_otp_email, name='send_otp_email'),
    path('validate_otp/', views.validate_otp, name='validate_otp'),
    path('success/',views.success_view,name='success'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('contact/', views.qrcode, name='qrcode'),
    path('hotels/', views.hotel_list, name='hotel_list'),  # List of hotels
    path('hotels/<int:hotel_id>/', views.select_room_type, name='select_room_type'),  # Select room type

    path('filter_hotels/', views.filter_hotels, name='filter_hotels'),
    path('hotels/<int:hotel_id>/room/<int:num_rooms>/confirm/<str:total_price>/', views.confirm_booking,
         name='confirm_booking'),


    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    path("index/", views.index, name="index"),
path("rooms/", views.rooms, name="rooms"),
path('booking.html', views.booking, name='booking'),

path('confirm_booking/', views.confirm_booking, name='confirm_booking'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

