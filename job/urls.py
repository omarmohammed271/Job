from django.urls import path,include
from . import views

app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='jobs'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_detail'),
]