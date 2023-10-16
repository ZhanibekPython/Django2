from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('rand_num/', views.rand_num, name='randnum'),
    path('stats/<int:num>', views.stats, name='stats'),
    path('add_art/<str:name>/<str:body>/<str:author>/<str:category>/', views.add_art, name='add_art'),
    path('upload/', views.add_image, name='add_image'),
]
