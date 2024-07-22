from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
  path('', post_list, name='post_list'),
  path('post_create/', post_create, name='post_create'),
  path('<int:post_id>/post_like', post_like, name='post_like'),
  path('<int:post_id>/comment_create', comment_create, name="comment_create"),
  path('<int:comment_id>/comment_delete', comment_delete, name="comment_delete"),
]