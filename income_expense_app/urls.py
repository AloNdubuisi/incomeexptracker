from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('why/', views.why, name='why'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('set_new_password/', views.set_new_password, name='set_new_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
