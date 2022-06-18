from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, ListView

from .utils import DataMixin
from .models import rating


class elementview(DataMixin, DetailView):
    model = rating
    template_name = 'main/anime_detail.html'
    context_object_name = 'element'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context()
        return dict(list(context.items()) + list(c_def.items()))

class MainView(DataMixin, View):
    template = 'main/index.html'

    def get(self, request):
        self.context = self.get_context(indexrtng=rating.objects.order_by('-id')[:4])
        return (render (request, self.template, self.context ))

class AboutView(DataMixin, View):
    template = 'main/contacts.html'

    def get(self, request):
        self.context = self.get_context()
        return (render (request, self.template, self.context ))



class RatingView(DataMixin, View):
    template = 'main/rating.html'

    def get(self, request):
        self.context = self.get_context(rtng=rating.objects.all())
        return (render(request, self.template, self.context))


class registerUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class loginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class Anime(DataMixin, ListView):
    model = rating
    template_name = 'main/anime.html'
    context_object_name = 'rating'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context()
        return dict(list(context.items()) + list(c_def.items()))

def logout_user(request):
    logout(request)
    return redirect('home')




