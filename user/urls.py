from .views import login,owner_create,group_list
from django.urls import path

urlpatterns = [
    path('login/',login,name='login'),
    path('group/all/',group_list,name='group'),
    path('owner-create/',owner_create,name='owner-create'),
]