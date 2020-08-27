from django.contrib import admin
# from rest_framework.authtoken.models import Token
from app.models import MovieDetail, GenreName, User

# Register your models here.
admin.site.register(User)
# admin.site.register(Token)
admin.site.register(MovieDetail)
admin.site.register(GenreName)
