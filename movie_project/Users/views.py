from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render 
from django.views.generic import TemplateView , ListView , DetailView
from django.shortcuts import render 
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import CustomUserCreationForm

def show(request,):
    return HttpResponse('wellcome') 
class UserRegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("login") 
class UserLoginView(LoginView):
    template_name = "login.html"
    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.request.user.pk}) 
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "user_profile"
    login_url = "login"