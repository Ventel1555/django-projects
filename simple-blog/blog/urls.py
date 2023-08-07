from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<slug:slug>',views.post_detail, name='post_detail'),
    path('',views.post_list, name='post_list')
]
