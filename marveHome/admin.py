from django.contrib import admin
from .models import FoodGallery, DrinkGallery, FoodEvent, DrinkEvent, Subscribe, Review

# Register your models here.


class FoodGalleryAdmin(admin.ModelAdmin):
    fields = [
        'food_img', 'food_name', 'food_slug',
        'food_price', 'food_desc', 'food_allergic'
    ]
    list_display = ['food_name', 'food_slug', 'food_price']
    prepopulated_fields = {'food_slug': ('food_name',)}


class DrinkGalleryAdmin(admin.ModelAdmin):
    fields = [
        'drink_img', 'drink_name', 'drink_slug',
        'drink_price', 'drink_desc', 'drink_allergic'
    ]
    list_display = ['drink_name', 'drink_slug', 'drink_price']
    prepopulated_fields = {'drink_slug': ('drink_name',)}


class FoodEventAdmin(admin.ModelAdmin):
    fields = [
        'food_img', 'food_name', 'food_price', 'food_time',
        'food_from_date', 'food_to_date'
    ]


class DrinkEventAdmin(admin.ModelAdmin):
    fields = [
        'drink_img', 'drink_name', 'drink_price', 'drink_time',
        'drink_from_date', 'drink_to_date'
    ]


class SubscribeAdmin(admin.ModelAdmin):
    fields = [
        'subscribe_email', 'subscribe_date', 'subscribe_time'
    ]


class ReviewAdmin(admin.ModelAdmin):
    fields = [
        'review_img', 'review_name', 'review_text',
        'review_date', 'review_time'
    ]


admin.site.register(FoodGallery, FoodGalleryAdmin)
admin.site.register(DrinkGallery, DrinkGalleryAdmin)
admin.site.register(FoodEvent, FoodEventAdmin)
admin.site.register(DrinkEvent, DrinkEventAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Review, ReviewAdmin)

