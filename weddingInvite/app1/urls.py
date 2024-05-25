from django.urls import path

from app1 import views

app_name = 'locations'

urlpatterns = [
    path('', views.GuestsView.as_view(), name='guest_list')
]