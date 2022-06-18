from django.shortcuts import render, redirect
from .models import Articles
from main.utils import DataMixin
from .forms import ArticlesForm
from django.views.generic import DetailView, ListView




class NewsHome(DataMixin, ListView):
    template_name = 'news/news_home.html'
    context_object_name = 'news_bydate'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Articles.objects.order_by('date')

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_context()
        return dict(list(context.items()) + list(c_def.items()))

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

    return render(request, 'news/create.html')