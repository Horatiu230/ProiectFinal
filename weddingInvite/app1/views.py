from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from app1.forms import InfirmationForm
from app1.models import ConfirmationOfPresence, Address
from app1.models import PersonalizedInvitation
import imgkit
import pdfkit

from weddingInvite.settings import API_KEY


# import wkhtmltoimage


class GuestsView(LoginRequiredMixin, ListView):
    model = ConfirmationOfPresence
    template_name = 'app1/guests_index.html'


    def get_queryset(self):
        return ConfirmationOfPresence.objects.filter(utilizator=self.request.user, active=True)


# Creare formular completare date invitati
class CreateGuestsView(LoginRequiredMixin, CreateView):
    model = ConfirmationOfPresence
    fields = ['prenume', 'nume', 'email', 'număr_telefon',
              'număr_adulți', 'număr_copii', 'confirmare_prezență']
    template_name = 'app1/guests_form.html'


    def get_success_url(self):
        return reverse('guests:guest_list')



# Modificare formular date invitati
class UpdateGuestsView(LoginRequiredMixin, UpdateView):
    model = ConfirmationOfPresence
    fields = ['prenume', 'nume', 'email', 'număr_telefon',
              'număr_adulți', 'număr_copii', 'confirmare_prezență']
    template_name = 'app1/guests_form.html'


    def get_success_url(self):
        return reverse('guests:guest_list')



# Creare formular pentru introducerea datelor personalizate in invitatie
class CreatePersonalizedInvitationView(LoginRequiredMixin, CreateView):
    model = PersonalizedInvitation
    fields = ['nume_mireasă', 'nume_mire', 'dată_eveniment', 'părinții_miresei', 'părinții_mirelui',
              'nume_nașă', 'nume_naș', 'nume_biserică', 'ora_cununie_religioasă', 'local_petrecere', 'ora_petrecere']
    template_name = 'app1/invitation_form.html'

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('guests:modified_invitation')



# Update date din invitatie
class UpdateInviteView(LoginRequiredMixin, UpdateView):
    model = PersonalizedInvitation
    fields = ['nume_mireasă', 'nume_mire', 'dată_eveniment', 'părinții_miresei', 'părinții_mirelui',
              'nume_nașă', 'nume_naș', 'nume_biserică', 'ora_cununie_religioasă', 'local_petrecere', 'ora_petrecere']
    template_name = 'app1/invitation_form.html'

    def get_success_url(self):
        return reverse('guests:modified_invitation')


# Listare invitatie modificata(parte client)
class ListModifiedInvitationView(LoginRequiredMixin, ListView):
    model = PersonalizedInvitation
    fields = ['nume_mireasă', 'nume_mire', 'dată_eveniment', 'părinții_miresei', 'părinții_mirelui',
              'nume_nașă', 'nume_naș', 'nume_biserică', 'ora_cununie_religioasă', 'local_petrecere', 'ora_petrecere']
    template_name = 'app1/invitation_modified.html'

    def get_queryset(self):
        return PersonalizedInvitation.objects.order_by('-id')[:1]

# Listare invitatie modificata(parte invitat) - aici cred ca pot conditiona ce navbar sa imi apara in functie de link-ul de pe care merg acolo.
class FinalInvitationView(LoginRequiredMixin, ListView):
    model = PersonalizedInvitation
    fields = ['nume_mireasă', 'nume_mire', 'dată_eveniment', 'părinții_miresei', 'părinții_mirelui',
              'nume_nașă', 'nume_naș', 'nume_biserică', 'ora_cununie_religioasă', 'local_petrecere', 'ora_petrecere']
    template_name = 'app1/invitation_final.html'

    def get_queryset(self):
        return PersonalizedInvitation.objects.order_by('-id')[:1]

# Stergere date dabel invitati
@login_required
def delete_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=False)
    return redirect('guests:guest_list')


# activare - in mod ascuns momentan
@login_required
def activate_location(request, pk):
    ConfirmationOfPresence.objects.filter(id=pk).update(active=True)
    return redirect('guests:guest_list')


# Home Page
class HomePage(TemplateView):
    template_name = 'app1/home.html'


# Mesaj confirmare pt invitat
@login_required
def confirmation_message(request):
    return render(request, 'app1/confirmation_message.html')


# Mesaj infirmare invitat
@login_required
def infirmation_message(request):
    return render(request, 'app1/infirmation_message.html')



# Creare formular confirmare de catre invitat
class CreateConfirmationView(LoginRequiredMixin, CreateView):
    model = ConfirmationOfPresence
    fields = ['prenume', 'nume', 'email', 'număr_telefon',
              'număr_adulți', 'număr_copii', 'confirmare_prezență']
    template_name = 'app1/confirmation_form.html'

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if ConfirmationOfPresence.objects.filter(id=self.object.id).exists():
            user_instance = ConfirmationOfPresence.objects.get(id=self.object.id)
            user_instance.save()
            content = (f'Invitatul: {user_instance.prenume} {user_instance.nume} a confirmat prezența la eveniment. \n'
                       f'O să participe {user_instance.număr_adulți} adulți și {user_instance.număr_copii} copii!')
            msg_html = render_to_string('app1/email_received.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Confirmare eveniment', from_email=user_instance.email, to=['haiduc.hory@gmail.com'])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('guests:confirmation')


# Completare date infirmare - am facut si fisier forms in care am folosir numai campurile dorite la infirmare
class Infirmation(LoginRequiredMixin, CreateView):
    template_name = 'app1/infirmation_form.html'
    form_class = InfirmationForm

    def form_valid(self, form):
        form.instance.utilizator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('guests:infirmation')


# Creare formular de salvare adrese aferente localului si Bisericii
class MapsViewUser(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['adresă_local', 'adresă_biserică']
    template_name = 'app1/mapsuser.html'

    def get_success_url(self):
        return reverse('guests:modified_invitation')


# API restaurant
class MapsRestaurantViewClient(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'app1/restaurant_location_api.html'

    def get_queryset(self):
        return Address.objects.order_by('-id')[:1]

    def get_success_url(self):
        return reverse('guests:clientrestaurantlocation')


# API Biserica
class MapsChurchViewClient(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'app1/church_location_api.html'

    def get_queryset(self):
        return Address.objects.order_by('-id')[:1]

    def get_success_url(self):
        return reverse('guests:clientchurchlocation')


def my_view(request):
    context = {
        'api_key': API_KEY,
    }
    return render(request, 'app1/restaurant_location_api.html', context)





# Aici ar mai fi trebuit un link pentru vizualizare locatie Biserica, dar nu am reusit nici cu cel de restaurant

# @login_required
# def email_message(request):
#     return render(request, 'app1/email_received.html')


# def export_template(request):
#     context = {'key': 'value'}
#     html_content = render_to_string('app1/invitation_final.html', context)
#     # imgkit.from_string(html_content, 'output.png')
#     pdfkit.from_string(html_content, 'output.pdf')
#     return render(request, 'app1/invitation_final.html', context)


























