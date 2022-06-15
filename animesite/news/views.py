from django.shortcuts import render, redirect
from .models import Articles
from main.models import rating
from .forms import ArticlesForm
from django.views.generic import DetailView


sidertng = rating.objects.order_by('-rating')[:4]   #  4 аниме с самым высоким рейтингом
news = Articles.objects.order_by('-id')[:1]     #  последняя добавленая новость
data = {
    'sidertng': sidertng,
    'news': news
}


def news_home(request):
    news_bydate = Articles.objects.order_by('date')
    data['news_bydate'] = news_bydate
    return render(request, 'news/news_home.html', data )

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    extra_context = data

def createnews(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'


    form = ArticlesForm()
    data['form'] = form
    data['error'] = error

    return render(request, 'news/create.html', data)