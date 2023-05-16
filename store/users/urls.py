from django.urls import path
from users.views import registration, login, profile

from django.contrib.auth import views as auth_views
from users import views as user_views

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    ]
