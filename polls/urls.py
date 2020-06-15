from django.urls import path

from polls.views import *

urlpatterns = [
    path('users/', user_list),
    path('users/<pk>/', user_details),
    path('groups/', group_list),
    path('users_raw/', users_raw),
    path('users_raw/<pk>/', user_details_raw),
]
