from django.urls import path
from .views import HomeView, FoodGalleryView, AboutView, DrinkGalleryView, EventView, ReviewView, FoodDetailView,  ContactView, AddReviewView, DrinkDetailView

app_name = 'marveHome'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('gallery/food/', FoodGalleryView.as_view(), name='food'),
    path('food/item/<slug:food_slug>/', FoodDetailView.as_view(), name='food_item'),
    path('gallery/drink/', DrinkGalleryView.as_view(), name='drink'),
    path('drink/item/<slug:drink_slug>/', DrinkDetailView.as_view(), name='drink_item'),
    path('about/', AboutView.as_view(), name='about'),
    path('event/', EventView.as_view(), name='event'),
    path('review/', ReviewView.as_view(), name='review'),
    path('add-review/', AddReviewView.as_view(), name='add_review'),
    path('contact/', ContactView.as_view(), name='contact'),
]
