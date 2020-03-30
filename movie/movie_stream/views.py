# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
	most_recent_movies=Movie.objects.order_by('-datetime')
	return render(request=request,
				  template_name="main/home.html",
				  context={"most_recent_movies":most_recent_movies})
#class Homeview(View):
#	template_name='main/home.html'
#	def get(self,request):
#		most_recent_movies=Movie.objects.order_by('-datetime')[:8]
#		return render(request,self.template_name,{'menu_active_items':'home','most_recent_movies':most_recent_movies})

def MovieView(request,id):
	""" This function is for displaying movie and showing comments of that movie."""
	movie=Movie.objects.get(id=id)
	if request.user.is_authenticated:
		print('user signed in')
		comment_form=CommentForm()
		#context['form']=comment_form

		comments=Comment.objects.filter(movie__id=id).order_by('-datetime')
		print(comments)
		return render(request=request,
				       template_name="main/movie.html",
				       context={"movie":movie,"comments":comments,"form":comment_form})
	else:
		messages.info(request, f"You have to login first")
		return redirect("movie_stream:homepage")

def CommentView(request):

	"""This function is for saving comment posted by the user."""
	if request.method=="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			text=form.cleaned_data['text']
			movie_id=request.POST['movie']
			movie=Movie.objects.get(id=movie_id)
			new_comment=Comment(text=text,user=request.user,movie=movie)
			new_comment.save()
			return HttpResponseRedirect('/movie/{}'.format(str(movie_id)))
		return HttpResponseRedirect('This is Register view. POST Request.')







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