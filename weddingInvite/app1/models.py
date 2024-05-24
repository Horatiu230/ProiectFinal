from django.db import models

# Create your models here.


class ConfirmationOfPresence(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    adults_number = models.IntegerField()
    kids_number = models.IntegerField()
    region = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} -> {self.last_name}'


