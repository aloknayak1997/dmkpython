from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'onboarding'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name="signup"),
]