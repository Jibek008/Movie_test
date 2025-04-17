
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

STATUS_CHOICES = (
    ('pro', 'pro'),
    ('simple', 'simple')
)
class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(50)],
                                           null=True,blank=True)
    phone_number = PhoneNumberField(null=True,blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Country(models.Model):
   country_name = models.CharField(max_length=32, unique=True)

   def __str__(self):
       return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=32)
    director_bio= models.TextField()
    director_ago = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(100)])
    director_image = models.ImageField(upload_to='director_images/')

    def __str__(self):
        return self.director_name

class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    actor_bio = models.TextField()
    actor_age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(110)])
    actor_image = models.ImageField(upload_to='actor_images/')

    def __str__(self):
       return self.actor_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ManyToManyField(Country,related_name='movie')
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ('144','144'),
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
    )
    types = MultiSelectField(max_length=16,choices=TYPE_CHOICES, max_choices=5)
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailers = models.FileField(upload_to='movie_trailers')
    movie_image = models.FileField(upload_to='movie_images')
    movie_status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='simple')


    def __str__(self):
        return self.movie_name



    def get_avg_rating(self):
        rating = self.get_avg_rating().all()
        if rating.exists():
            return round(sum(i.stars for i in rating)/  rating.count(), 1)
        return 0

class MovieLanguages(models.Model):
    language =  models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_languages/')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='movie_videos')

    def __str__(self):
        return self.language

class Moments(models.Model):
  movie = models.ForeignKey(Movie, on_delete=CASCADE, related_name='movie_moments')
  movie_moments = models.ImageField(upload_to='movie_moments/')

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rantings')
    stars  = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)],null=True,blank=True)
    parent =models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.movie}'

class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=CASCADE)

class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.movie}'
