
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.HelloView.as_view(), name="user_data"),

]