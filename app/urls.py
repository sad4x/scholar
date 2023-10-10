from django.urls import path
from .views import main, login

urlpatterns = [
    path('', main),
    path('login/', login)
]