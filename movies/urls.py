from django.urls import path
from .views import MoviesView, MoviesDetailViews, MoviesOrderViews


urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path('movies/<int:movie_id>/', MoviesDetailViews.as_view()),
    path('movies/<int:movie_id>/orders/', MoviesOrderViews.as_view()),
]
