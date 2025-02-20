from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('news_create/', views.news_create_view, name='news_create'),
    path('car_create/', views.car_create_view),
    path('car_detail/<int:pk>/', views.car_detail_view, name='detail'),
    path('car_create_2/', views.car_create_view_2),
    path('car_detail_2/<int:pk>/', views.car_detail_view_2, name='detail_2'),
    path('car_delete/<int:pk>/', views.car_delete_view, name='delete')
]
