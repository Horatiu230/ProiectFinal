from django.shortcuts import render
from django.views.generic import ListView
from app1.models import ConfirmationOfPresence


class GuestsView(ListView):
    model = ConfirmationOfPresence
    template_name = 'app1/guests_index.html'
