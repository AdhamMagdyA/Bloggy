from django.urls import path
from . import views

# namespace the app to articles
app_name = 'articles'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<slug:article_slug>/edit/', views.edit, name='edit'),
    path('<slug:article_slug>/delete/', views.delete, name='delete'),
    path('<slug:article_slug>/', views.get, name='get')
]