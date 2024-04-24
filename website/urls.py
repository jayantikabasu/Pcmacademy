"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from update import views as MainApp_views
from BlogApp import views as BlogApp_views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainApp_views.index, name='index'),
    path('index/', MainApp_views.index, name='index'),
    path('applyfrom/', MainApp_views.applyform, name='applyform'),
    path('get_quote/', MainApp_views.get_quote, name='get-a-quote'),
    path('about/',MainApp_views.about, name='about'),
    path('course/', MainApp_views.course, name='course'),
    path('course_details/<int:pk>', MainApp_views.course_details, name='course_details'),
    path('faculty/', MainApp_views.faculty, name='faculty'),
    path('contact/', MainApp_views.contact, name='contact'),
    path('blog/', BlogApp_views.blog, name='blog'),
    path('show_blog/<slug:slug>',BlogApp_views.show_blog, name='show_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)