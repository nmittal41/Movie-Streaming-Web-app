from django.contrib import admin
from django.urls import path,include
from . import views

app_name='movie_stream'

urlpatterns= [

		path('',views.homepage,name='homepage'),
		path('register/',views.register,name='register'),
		path('login/',views.login_request,name='login'),
		path('logout/',views.logout_request,name='logout'),
		path('profile/',views.view_profile,name='profile'),
		path('movie/<int:id>',views.MovieView,name='MovieView'),


]