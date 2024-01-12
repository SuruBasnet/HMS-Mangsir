from django.urls import path
from.views import *

urlpatterns = [
    path('employee-info/all/',EmployeeInfoView.as_view({'get':'list','post':'create'}),name='employee-info')
]