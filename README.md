# Movie Streaming Web-app
>This is simple movie streaming web-app build using Python-Django.

## Tech Stack
- Django - Backend
- HTML, CSS, Javascript - Front End
- SQLite3 - Database

## Setup

### Clone the repository
git clone https://github.com/nmittal41/Movie-Streaming-Web-app.git 

### Installation
Run :
```
python manage.py createsuperuser
```

This super user can access the admin side ('/admin').
This super user can also sign in and add or remove movies.
This super user also have control over comments posted.

Run the server using:
```
python manage.py runserver
```



## Technical Approach
- To add a movie I have made a path field in which it contains the link of movie.
- User can watch movie only if he is logged in.
- User can also add comments on movie.
- Currently in this project I have used some movies from youtube.
- To add a movie from youtube provide link e.g https://www.youtube.com/embed/{video id}  