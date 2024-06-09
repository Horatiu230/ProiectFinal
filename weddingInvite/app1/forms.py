from django import forms

from app1.models import ConfirmationOfPresence


class InfirmationForm(forms.ModelForm):

    class Meta:
        model = ConfirmationOfPresence
        fields = ['prenume', 'nume', 'email', 'confirmare_prezență']


        def clean_număr_telefon(self):
            val = self.cleaned_data.get('număr_telefon')
            if val is None:
                return None
            return val
        def clean_număr_adulți(self):
            val = self.cleaned_data.get('număr_adulți')
            if val is None:
                return None
            return val

        def clean_număr_copii(self):
            val = self.cleaned_data.get('număr_copii')
            if val is None:
                return None
            return val

        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.save(update_fields=['prenume', 'nume', 'email', 'confirmare_prezență'])
            return instance
