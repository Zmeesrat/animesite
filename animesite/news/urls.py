from django.urls import path
from .views import *


urlpatterns = [
   path('', NewsHome.as_view(), name='news_home'),
   path('create', createnews, name='createnews'),
   path('<int:pk>/', NewsDetailView.as_view(), name='news-detail')
]