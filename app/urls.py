from django.urls import path
from .views import main, login_u, logout_u, register_u

urlpatterns = [
    path('', main),
    path('login/', login_u),
    path('logout/', logout_u),
    path('register/',register_u)
]