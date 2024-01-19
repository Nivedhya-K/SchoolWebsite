from .import views
from django.urls import path
app_name='schoolapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('form', views.form, name='form'),
    path('button',views.form,name='button'),
]