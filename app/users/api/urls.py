from django.urls import path

from app.users.api.api import  user_api_view, user_detail_view

urlpatterns = [
    path('users/', user_api_view, name='user_api_view'),
    path('users/<int:pk>/', user_detail_view, name='usuario_detail_api_view')
    #path('user/<slug:string>/', user_detail_view, name='usuario_detail_api_view')
    #path('user/<int:pk>/', user_detail_view_delete, name='usuario_detail_api_view_delete')
]