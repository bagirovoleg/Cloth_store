from django.urls import path
from users.views import registration, login, profile, logout

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
