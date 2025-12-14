from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.views.generic import TemplateView , ListView , DetailView
from .models import Movie , Director , Actor , MovieActor , FilmCritic , ImageGallery , MusicAlbum , PhotosofTheActors 

def show(request,):
    return HttpResponse('wellcome')

class HomePage(TemplateView):  
    template_name = "home.html" 
    
    def get_context_data(self,**kwargs): 
        context = super().get_context_data(**kwargs) 
        context["movies"] = Movie.objects.all()[:100] 
        context["actors"] = Actor.objects.all()[:100] 
        context["movieactor"] = Movie.objects.all() 
        return context 

    def render_to_response(self, context, **response_kwargs):
        
        return render(self.request, self.template_name, context, **response_kwargs)  
class SearchPage(ListView):
    template_name = "search.html" 
    context_object_name = 'movies' 
    model = Movie 
    
    def get_queryset(self):
        query = self.request.GET.get("word", "")
        if query:
            return Movie.objects.filter(Title__icontains=query).distinct()
        return Movie.objects.all()

    
    def render_to_response(self, context, **response_kwargs):
        
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            movies = context['movies']
            results = [{"id": str(m.Movie_id), "title": m.Title} for m in movies]
            return JsonResponse({"results": results})
        
        
        return render(self.request, self.template_name, context, **response_kwargs) 
class MovieDetailPage(DetailView): 
      model = Movie
      template_name = "moviedetail.html" 
      context_object_name = "movie" 
class ActorOrDirectorDetailPage(DetailView): 
      model = Actor 
      template_name = "actorordirectordetail.html" 
      context_object_name= "actorordirector" 
      
      def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs) 
           context["director"] = Director.objects.all() 
           return context 
class MovieByGenreView(ListView):
    model = Movie
    template_name = "movies_by_genre.html"
    context_object_name = "movies"

    def get_queryset(self):
        genre_code = self.kwargs.get("genre") 
        if genre_code == "All":
           return Movie.objects.all()
        return Movie.objects.filter(Genre=genre_code)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_code = self.kwargs.get("genre")
        genre_name = dict(Movie.GENRE_CHOICES).get(genre_code, "Unknown")
        context["genre_name"] = genre_name
        return context