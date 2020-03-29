# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
	most_recent_movies=Movie.objects.order_by('-datetime')[:8]
	return render(request=request,
				  template_name="main/home.html",
				  context={"most_recent_movies":most_recent_movies})
#class Homeview(View):
#	template_name='main/home.html'
#	def get(self,request):
#		most_recent_movies=Movie.objects.order_by('-datetime')[:8]
#		return render(request,self.template_name,{'menu_active_items':'home','most_recent_movies':most_recent_movies})

def MovieView(request,id):
	movie=Movie.objects.get(id=id)
	return render(request=request,
				  template_name="main/movie.html",
				  context={"movie":movie})











def register(request):
	if request.method=="POST":
		form=NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f"New account created for :{username}")
			login(request, user)
			messages.info(request,f"You are now logged in as {username}")
			#return redirect("main:homepage")
			return redirect("movie_stream:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")
	form=NewUserForm
	return render(request,
				  "main/register.html",
				  context={"form":form})

def login_request(request):
	if request.method=="POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("movie_stream:homepage")
			else:
				messages.error(request,"Invalid username or password")

	form=AuthenticationForm()
	return render(request,
			      "main/login.html",
			      {"form":form})

def logout_request(request):
	logout(request)
	messages.info(request,"Logged out succesfully")
	return redirect("movie_stream:homepage")


@login_required
def view_profile(request):
  args = {'user': request.user}
  return render(request, 'main/profile.html', args)