from django.urls import path
from .views import *

urlpatterns = [
   path('', MainView.as_view(), name='home'),
   path('about', AboutView.as_view(), name='about'),
   path('anime', Anime.as_view(), name='anime'),
   path('rating', RatingView.as_view(), name='rating'),
   path('register', registerUser.as_view(), name='register'),
   path('login', loginUser.as_view(), name='login'),
   path('logout', logout_user, name='logout'),
   path('<slug:slug>', elementview.as_view(), name='element')
]