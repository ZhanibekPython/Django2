from . import views
from django.urls import path

urlpatterns = [
    path('', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>', views.post, name='post'),
]
