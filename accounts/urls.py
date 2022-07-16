from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #path(r'^$', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('ajax/', views.ajax, name='register'),
    #path(r'^profile/$', views.profile, name='profile'),
    #path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]