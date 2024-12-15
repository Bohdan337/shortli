from django.urls import path
from . import views

urlpatterns = [
    path('my_url', views.users_url, name='my_url'),
    path('', views.create_short_url, name='main'),
    path('url/<str:short_code>/', views.redirect_to_original, name='redirect'),
]