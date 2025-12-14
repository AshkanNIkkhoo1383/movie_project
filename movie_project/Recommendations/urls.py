from django.urls import path , re_path
from django.contrib import admin 
from .views import CombinedRecommendationView
from Movie import apps
from . import views 

apps_name = 'Recommendations' 

urlpatterns = [
       re_path(r'^$',views.show,name='show'), 
       path('recommendations/', CombinedRecommendationView.as_view(), name='recommendations'),
          ]
