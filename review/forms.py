from django.contrib.auth import get_user_model
from django import forms
from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    # edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # Permet l'insertion d'un champ 'edit_ticket' caché afin de montrer que le formulaire proposé est en édition
    # Il sert de discriminant

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class DeleteTicketForm(forms.ModelForm):
    # delete_ticket = forms.BooleanField(initial=True)
    # Permet l'insertion d'un champ caché servant de discriminant
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    # edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    # Permet l'insertion d'un champ caché servant de discriminant

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class DeleteReviewForm(forms.ModelForm):
    # delete_ticket = forms.BooleanField(initial=True)
    # Permet l'insertion d'un champ caché servant de discriminant
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


class UserFollowsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
