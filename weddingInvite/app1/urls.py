from django.urls import path
from weddingInvite.app1 import views

app_name = 'guests'

urlpatterns = [
    path('', views.GuestsView.as_view(), name='guest_list')
]