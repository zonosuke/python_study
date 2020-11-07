from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
  path('', views.PostList.as_view(), name='post_list'),
  path('detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail')
]