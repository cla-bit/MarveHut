from django import forms
from .models import Review, Subscribe


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['review_img', 'review_name', 'review_text']


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['subscribe_email']

