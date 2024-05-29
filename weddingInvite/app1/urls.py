from django.urls import path

from app1 import views

app_name = 'guests'

urlpatterns = [
    path('', views.GuestsView.as_view(), name='guest_list'),
    path('add/', views.CreateGuestsView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateGuestsView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_location, name='delete'),
    path('<int:pk>/activate/', views.activate_location, name='activate')
]