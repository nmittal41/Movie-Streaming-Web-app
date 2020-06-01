from django.forms import ModelForm
from movies.models import Movie, Comment

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__' 
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

