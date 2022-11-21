from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class FoodGallery(models.Model):
    food_img = models.ImageField(upload_to='food_pics')
    food_name = models.CharField(max_length=50, null=True)
    food_slug = models.SlugField(max_length=50, unique=True, null=True)
    food_price = models.IntegerField(default=0)
    food_desc = models.TextField()
    food_allergic = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse('marveHome:food_item', args=[self.food_slug])


class DrinkGallery(models.Model):
    drink_img = models.ImageField(upload_to='drink_pics')
    drink_name = models.CharField(max_length=50, null=True)
    drink_slug = models.SlugField(max_length=50, unique=True, null=True)
    drink_price = models.IntegerField(default=0)
    drink_desc = models.TextField()
    drink_allergic = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.drink_name

    def get_absolute_url(self):
        return reverse('marveHome:drink_item', args=[self.drink_slug])


class FoodEvent(models.Model):
    food_img = models.ImageField(upload_to='event_food_pics')
    food_name = models.CharField(max_length=50, null=True)
    food_price = models.IntegerField(default=0)
    food_time = models.TimeField(default=timezone.now())
    food_from_date = models.DateField(default=date.today())
    food_to_date = models.DateField(default=date.today())

    def __str__(self):
        return self.food_name


class DrinkEvent(models.Model):
    drink_img = models.ImageField(upload_to='event_drink_pics')
    drink_name = models.CharField(max_length=50, null=True)
    drink_price = models.IntegerField(default=0)
    drink_time = models.TimeField(default=timezone.now())
    drink_from_date = models.DateField(default=date.today())
    drink_to_date = models.DateField(default=date.today())

    def __str__(self):
        return self.drink_name


class Subscribe(models.Model):
    subscribe_email = models.EmailField()
    subscribe_date = models.DateField(default=date.today())
    subscribe_time = models.TimeField(default=timezone.now())

    def __str__(self):
        return self.subscribe_email


class Review(models.Model):
    review_img = models.ImageField(upload_to='review_pics',
                                   default='review_pics/default-user.png',
                                   blank=True, null=True)
    review_name = models.CharField(max_length=100, null=True)
    review_text = models.TextField()
    review_date = models.DateField(default=date.today())
    review_time = models.TimeField(default=timezone.now())

    def __str__(self):
        return self.review_name



