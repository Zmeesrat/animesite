from .forms import *
from .models import *
from news.models import *


class DataMixin:
    def get_context(self, **kwargs):
        context = kwargs
        context['sidebarlogform'] = LoginForm
        context['sidertng'] = rating.objects.order_by('-rating')[:4]
        context['news'] = Articles.objects.order_by('-id')[:1]
        return context