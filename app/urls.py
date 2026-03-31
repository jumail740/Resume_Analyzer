from django.urls import path
from .views import home
from .views import home, register_view, login_view, logout_view,dashboard

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
     path('dashboard/', dashboard, name='dashboard'),
]   