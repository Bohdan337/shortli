from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout')
]