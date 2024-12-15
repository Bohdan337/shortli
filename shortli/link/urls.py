from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('url/create/', views.create_short_url, name='main'),
    path('url/<str:short_code>/', views.redirect_to_original, name='redirect'),
]