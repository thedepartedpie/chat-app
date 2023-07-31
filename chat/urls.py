from django.urls import path
from django.contrib.auth import views as auth_views
from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='home'),
    path('chat/<int:reciever_id>/', views.chat, name='chat'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('register', views.register, name='register')
]