from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class TourAgency(models.Model):
    """
    Tour agency model to add information about the agency, give
    description of its services and its location.
    """
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    description = models.TextField(
        blank=True, help_text='Warning editing this'
        'field will change the About Us section on the home page!')

    def __str__(self):
        return self.name


class Season(models.Model):
    """
    Season model to add the name of season in
    which the packages will be available, and the information about when
    a season starts and ends.
    """
    name = models.CharField(max_length=10)
    start = models.CharField(max_length=15)
    end = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Package(models.Model):
    """
    Packages model to add information about packages, the seasons they
    are available,the start place, duration etc.
    """
    GSIZES = ((4, "Four"), (8, "Eight"), (12, "Tweleve"), (16, "Sixteen"))
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='packages')
    title = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=100, unique=True, default='')
    duration = models.CharField(max_length=50, default="3 days")
    start_place = models.CharField(max_length=50, default="Kabul")
    end_place = models.CharField(max_length=50, default="Bamyan")
    group_size = models.IntegerField(choices=GSIZES, default=4)
    description = models.TextField(
        blank=False, default="No description is provided!")
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    """ 
    Reviews model to get reviews from users about packages and their experience
    """
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"

