from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from movies.models import Movie, Comment
from movies.forms import CommentForm


class MovieDetailsForm(UserPassesTestMixin,CreateView):
    '''
    View for Creating Movie add form:
        - Uses movie model and take all fields
    Permissions:
        - Only Admin allowed
    '''

    model = Movie
    fields = '__all__'
    success_url = '/movies'
    def test_func(self):
        return self.request.user.is_superuser
class MovieDetailsUpdate(UserPassesTestMixin,UpdateView):
    '''
    View for Movie Details Update:
        - Uses Movie model, takes id from url and Uses Update View generic template to create a update form
    Permission:
        - Only Admin allowed
    '''

    model = Movie
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/movies'
    def get_object(self):
        return Movie.objects.get(id = self.kwargs['id'])

    def test_func(self):
        return self.request.user.is_superuser

class MovieDetails(LoginRequiredMixin,DetailView):
    '''
    View for Movie Detail Page:
        - Uses Detail View for displaying information about a movie
        - takes id of movie from url and get object returns the respective movie 
    Permission:
        - Only Login User
    '''

    def get_object(self):
        post = Movie.objects.get(id = self.kwargs['id'])

        # Returning the comment form, post, and comments till now
        return {'detail':post,'form':CommentForm,'comment':Comment.objects.filter(post = post)}
    template_name = 'movies/movie_details.html'
    query_set = Movie.objects.all()

class AllMovies(LoginRequiredMixin,ListView):
    '''
    View for All Movies List:
        - Uses List View from generic template to create a list of objects
    Permission:
        - Only Login User
    '''

    model = Movie

class CommentFormView(LoginRequiredMixin,FormView):
    '''
    View for handling comment section:
        - Creates a simple form and handles the linkage of each comment with user
          and post
        - Takes user id from request user
        - Takes post id from link
    Permission:
        - Only Login User

    '''

    form_class = CommentForm
    success_url = '/movies'
    def form_valid(self,form):
        id = self.kwargs['id']
        print(self.request.user)
        form.instance.user = self.request.user
        form.instance.post = Movie.objects.get(id=id)
        form.save()
        return super().form_valid(form)
