from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from app1.models import ConfirmationOfPresence
from app1.models import PersonalizedInvitation


class GuestsView(LoginRequiredMixin, ListView):
    model = ConfirmationOfPresence
    template_name = 'app1/guests_index.html'


class CreateGuestsView(LoginRequiredMixin, CreateView):
    model = ConfirmationOfPresence
    fields = ['prenume', 'nume', 'email', 'număr_telefon',
              'număr_adulți', 'număr_copii']
    template_name = 'app1/guests_form.html'

    def get_success_url(self):
        return reverse('guests:guest_list')


class CreatePersonalizedInvitationView(LoginRequiredMixin, CreateView):
    model = PersonalizedInvitation
    fields = ['nume_mireasă', 'nume_mire', 'dată_eveniment', 'părinții_miresei', 'părinții_mirelui',
              'nume_nașă', 'nume_naș', 'nume_biserică', 'ora_cununie_religioasă', 'local_petrecere', 'ora_petrecere']
    template_name = 'app1/invitation_form.html'

    def get_success_url(self):
        return reverse('guests:personalized_invitation')


class UpdateGuestsView(LoginRequiredMixin, UpdateView):
    model = ConfirmationOfPresence
    fields = ['first_name', 'last_name', 'email', 'phone_number',
              'adults_number', 'kids_number', 'region']
    template_name = 'app1/guests_form.html'

    def get_success_url(self):
        return reverse('guests:guest_list')


@login_required
def delete_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=False)
    return redirect('guests:guest_list')


@login_required
def activate_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=True)
    return redirect('guests:guest_list')


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'app1/home.html'

































