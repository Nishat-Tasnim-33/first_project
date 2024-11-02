from django.contrib import admin
from django.urls import path
from first_app.views.fbv_views import book_list

urlpatterns = [
   
    path('fbv/',book_list, name = 'book_list'),
]
