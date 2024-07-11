from django.urls import path
from .views import *

app_name='reviews'

urlpatterns = [
    path('', review_list), #localhost: 8000/reviews
    path('/create', review_create), #localhost: 8000/reviews/create
    path('/<int:id>', review_detail),
    path('/<int:id>/update', review_update),
    path('/<int:id>/delete', review_delete),
]