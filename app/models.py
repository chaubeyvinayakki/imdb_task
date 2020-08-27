# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Store User account details.
    """
    username = models.CharField('username', max_length=85, unique=True,)
    name = models.CharField('name', max_length=80, null=True, blank=True)
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['name', ]

    def __str__(self):
        return '<{id}>: {email}'.format(
            id=self.id,
            email=self.email,
        )


class GenreName(models.Model):
    """
    GenreName model used to save the Genre of the movie
    """
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "genre_name"

    def __str__(self):
        return self.name


class MovieDetail(models.Model):
    """
    MovieDetail model used to save the Movie details
    """
    name = models.CharField(max_length=300, blank=True, null=True)
    imdb_score = models.FloatField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    director = models.CharField(max_length=300, blank=True, null=True)
    genre = models.ManyToManyField(GenreName)

    class Meta:
        verbose_name = "movie"

    def __str__(self):
        return self.name



