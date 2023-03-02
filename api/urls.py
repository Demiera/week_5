from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ReadAPIView.as_view(), name='Read_API'),
    path('api/<pk>/', views.DetailAPIView.as_view(), name='detail_API'),
]