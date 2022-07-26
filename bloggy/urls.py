from django.contrib import admin
from django.urls import path, include
from bloggy import settings, views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('captcha/', include('captcha.urls')),

    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)