from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    #path('button',views.button,name="button"),
    #path('get_courses/', views.get_courses, name='get_courses'),
    path('sampleform/',views.sampleform,name='sampleform'),
    path('submit_form',views.submit_form,name='submit_form'),
    #path('order_confirm',views.order_confirm,name='order_confirm'),
    path('logout',views.logout,name='logout')
]
