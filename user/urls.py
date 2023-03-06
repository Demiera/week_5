from django.urls import path
from user import views

urlpatterns = [
    path('topic/', views.ReadAPIView.as_view(), name='Read_API'),
    path('topic/<int:pk>/', views.DetailAPIView.as_view(), name='detail_API'),
    path('user/', views.UserListView.as_view(), name='User_Read_API'),
    path('user/<int:pk>/', views.UserRetrieveView.as_view(), name='User_detail_API'),
]