from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('', main, name='main'),
    path('signup/', signup, name='signup'),
]