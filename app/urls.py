from django.urls import path
from .views import SearchMovie, Admin, User

app_name = 'app'

urlpatterns = [
    path('movie-detail/', SearchMovie.as_view(), name='movie-detail'),
    path('admin-movie/', Admin.as_view(), name='admin_create_movie'),
    path('get-movie/', User.as_view(), name='admin_create_movie'),
]
