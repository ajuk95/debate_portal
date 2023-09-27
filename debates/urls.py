# debates/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('debates/', views.debate_list, name='debate_list'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
