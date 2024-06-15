from django import forms

from app1.models import ConfirmationOfPresence


class InfirmationForm(forms.ModelForm):

    class Meta:
        model = ConfirmationOfPresence
        fields = ['prenume', 'nume', 'confirmare_prezență']







        # def clean(self):
        #     cleaned_data = super().clean()
        #     prenume = cleaned_data.get('prenume')
        #     nume = cleaned_data.get('nume')
        #
        #     if ConfirmationOfPresence.objects.filter(prenume=prenume, nume=nume).exists():
        #         raise forms.ValidationError("Combinația de nume există deja.")
        #     return cleaned_data


        # def clean_număr_telefon(self):
        #     val = self.cleaned_data.get('număr_telefon')
        #     if val is None:
        #         return ''
        #     return ''
        # def clean_număr_adulți(self):
        #     val = self.cleaned_data.get('număr_adulți')
        #     if val is None:
        #         return ''
        #     return ''
        # #
        # def clean_număr_copii(self):
        #     val = self.cleaned_data.get('număr_copii')
        #     if val is None:
        #         return ''
        #     return val

