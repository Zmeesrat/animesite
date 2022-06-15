from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('about', views.about, name='about'),
   path('anime', views.anime, name='anime'),
   path('rating', views.rating_page, name='rating'),
   path('register', views.registerUser.as_view(), name='register'),
   path('login', views.loginUser.as_view(), name='login'),
   path('logout', views.logout_user, name='logout'),
   path('<slug:slug>', views.elementview.as_view(), name='element')
]