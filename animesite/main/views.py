from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import rating
from .forms import LoginForm
from django.views.generic import DetailView, CreateView
from news.models import Articles


rtng = rating.objects.all()     # список аниме для таблице на странице "рейтинг"
indexrtng = rating.objects.order_by('-id')[:4]      #  4 последних добавленых аниме
sidertng = rating.objects.order_by('-rating')[:4]   #  4 аниме с самым высоким рейтингом
news = Articles.objects.order_by('-id')[:1]     #  последняя добавленая новость
sidebarlogform = LoginForm
data = {
    'sidebarlogform': sidebarlogform,
    'sidertng': sidertng,
    'news': news
}

class elementview(DetailView):
    model = rating
    template_name = 'main/anime_detail.html'
    context_object_name = 'element'
    extra_context = data


def index(request):
    data['indexrtng'] = indexrtng
    return render(request, 'main/index.html', data)

def about(request):
   return render(request, 'main/contacts.html', data)

def anime(request):
   return render(request, 'main/anime.html', data)

def rating_page(request):
    data['rtng'] = rtng
    return render(request, 'main/rating.html', data )

class registerUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class loginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')




