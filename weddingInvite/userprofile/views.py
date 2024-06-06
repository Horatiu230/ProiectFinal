import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from userprofile.forms import NewAccountForm


class CreateNewAccount(CreateView):
    template_name = 'registration/new_user.html'
    form_class = NewAccountForm

    def get_success_url(self):
        pswd = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '!$%&?@') for _ in range(8))
        print(pswd)
        if User.objects.filter(id=self.object.id).exists():
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(pswd)
            user_instance.save()
            content = f'Datele tale de autentificare sunt: \n {user_instance.username} \n {pswd}'
            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Date conectare aplicatie', body=content,
                                           from_email='sendemailcontact@demo.ro', to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('login')




