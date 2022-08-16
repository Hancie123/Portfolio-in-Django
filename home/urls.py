from django.contrib import admin
from django.urls import path,include
from home import views



admin.site.site_header='Hancie Phago'
admin.site.site_title="Welcome to Hancie Phago Dashboard"
admin.site.index_title="Hancie Phago Portal"
admin.site
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]