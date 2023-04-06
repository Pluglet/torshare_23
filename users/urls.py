from django.urls import path

from .views import user_list, register_login


urlpatterns = [
    path('user_list', user_list, name='user_list'),
    path('', register_login, name='register_login'),
]
