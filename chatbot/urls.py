from django.urls import path
from .views import home, chat_api, register, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/chat/', chat_api, name='chat_api'),
]