from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from userprofile.forms import NewAccountForm


class CreateNewAccount(CreateView):
    template_name = 'app1/new_user.html'
    form_class = NewAccountForm

    def get_success_url(self):
        return reverse('home')