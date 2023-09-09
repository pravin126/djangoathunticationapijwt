
from django.urls import path, include
from account.views import UserRegistationView   

urlpatterns = [
    path("register/", UserRegistationView.as_view(),name='register'),

]
