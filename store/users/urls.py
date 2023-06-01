from django.urls import path
from users.views import UserRegistrationView, login, UserProfileView, logout

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
