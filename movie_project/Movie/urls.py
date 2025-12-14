from django.urls import path , re_path
from django.contrib import admin
from Movie import apps 
from .views import SearchPage , HomePage , MovieDetailPage , ActorOrDirectorDetailPage , MovieByGenreView
from . import views 

apps_name = 'Movie' 

urlpatterns = [ 
       re_path(r'^$',views.show,name='show'),
       re_path(r'home/',HomePage.as_view(),name='home'), 
       re_path('search/',SearchPage.as_view(),name='search'), 
       re_path('moviedetail/<int:pk>/',MovieDetailPage.as_view(),name='movie'),
       re_path('actorordirectordetail/<int:pk>/',ActorOrDirectorDetailPage.as_view(),name='actorordirector'), 
       path("movies/genre/<str:genre>/", MovieByGenreView.as_view(), name="movies_by_genre"),
    ]
