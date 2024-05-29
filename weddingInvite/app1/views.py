from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from app1.models import ConfirmationOfPresence


class GuestsView(ListView):
    model = ConfirmationOfPresence
    template_name = 'app1/guests_index.html'


class CreateGuestsView(CreateView):
    model = ConfirmationOfPresence
    fields = ['first_name', 'last_name', 'email', 'phone_number',
              'adults_number', 'kids_number', 'region']
    template_name = 'app1/guests_form.html'

    def get_success_url(self):
        return reverse('guests:guest_list')


class UpdateGuestsView(UpdateView):
    model = ConfirmationOfPresence
    fields = ['first_name', 'last_name', 'email', 'phone_number',
              'adults_number', 'kids_number', 'region']
    template_name = 'app1/guests_form.html'

    def get_success_url(self):
        return reverse('guests:guest_list')


def delete_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=False)
    return redirect('guests:guest_list')



def activate_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=True)
    return redirect('guests:guest_list')
































