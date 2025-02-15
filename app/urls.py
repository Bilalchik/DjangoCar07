from django.urls import path
from . import views


urlpatterns = [
    path('news_create/', views.news_create_view, name='news_create'),
    path('car_create/', views.car_create_view),
]
