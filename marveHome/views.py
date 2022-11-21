from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from .models import FoodEvent, DrinkEvent, Review, FoodGallery, DrinkGallery
from .forms import AddReviewForm, SubscribeForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    template_name = 'home/index.html'
    model = FoodGallery
    context_object_name = 'food'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drink'] = DrinkGallery.objects.all()[:4]
        context['event_food'] = FoodEvent.objects.all()
        context['event_drink'] = DrinkEvent.objects.all()
        context['reviews'] = Review.objects.all().order_by('-review_time')[:7]
        return context

    def get_queryset(self):
        food = FoodGallery.objects.all()[:8]
        return food


class FoodGalleryView(ListView):
    template_name = 'home/food.html'
    model = FoodGallery
    context_object_name = 'food'
    queryset = FoodGallery.objects.all()
    ordering = ['-id']
    paginate_by = 8


class FoodDetailView(DetailView):
    template_name = 'home/food_order.html'
    model = FoodGallery
    context_object_name = 'food'
    query_pk_and_slug = 'food_slug'
    slug_field = 'food_slug'
    slug_url_kwarg = 'food_slug'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class DrinkGalleryView(ListView):
    template_name = 'home/drink.html'
    model = DrinkGallery
    context_object_name = 'drink'
    queryset = DrinkGallery.objects.all()
    ordering = ['-id']
    paginate_by = 8


class DrinkDetailView(DetailView):
    template_name = 'home/drink_order.html'
    model = DrinkGallery
    context_object_name = 'drink'
    slug_url_kwarg = 'drink_slug'
    query_pk_and_slug = 'drink_slug'
    slug_field = 'drink_slug'


class EventView(TemplateView):
    template_name = 'home/event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_food'] = FoodEvent.objects.all()
        context['event_drink'] = DrinkEvent.objects.all()
        return context


class ReviewView(TemplateView):
    template_name = 'home/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all().order_by('-review_time')
        return context


class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('marveHome:contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddReviewView(CreateView):
    template_name = 'home/add_review.html'
    model = Review
    form_class = AddReviewForm
    success_url = reverse_lazy('marveHome:review')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
