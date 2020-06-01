"""moviestreaming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from movies.views import AllMovies, MovieDetails, CommentFormView, MovieDetailsForm, MovieDetailsUpdate
urlpatterns = [
    path('', AllMovies.as_view(), name='AllMovies' ),
    path('<int:id>', MovieDetails.as_view()),
    path('create/', MovieDetailsForm.as_view(), name='MovieDetailsForm' ),
    path('update/<int:id>', MovieDetailsUpdate.as_view(), name = 'MovieDetailsUpdate'),
    path('comment/<int:id>',CommentFormView.as_view()),
]
