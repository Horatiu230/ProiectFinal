from django.urls import path

from app1 import views

app_name = 'guests'

urlpatterns = [
    path('', views.GuestsView.as_view(), name='guest_list'),
    path('personalize/', views.CreatePersonalizedInvitationView.as_view(), name='personalized_invitation'),
    path('<int:pk>/updateinvite/', views.UpdateInviteView.as_view(), name='update_invite'),
    path('finalinvite/', views.FinalInvitationView.as_view(), name='final_invitation'),
    path('modifiedinvite/', views.ListModifiedInvitationView.as_view(), name='modified_invitation'),
    path('add/', views.CreateGuestsView.as_view(), name='add'),
    path('confirmation/', views.CreateConfirmationView.as_view(), name='confirmation_form'),
    path('infirmation/', views.Infirmation.as_view(), name='infirmation_form'),
    path('<int:pk>/update/', views.UpdateGuestsView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_location, name='delete'),
    path('<int:pk>/activate/', views.activate_location, name='activate'),
    path('confirmationmessage/', views.confirmation_message, name='confirmation'),
    path('infirmationonmessage/', views.infirmation_message, name='infirmation'),
    path('churchpartylocations/', views.MapsViewUser.as_view(), name='churchpartylocations'),
    path('clientrestaurantlocation/', views.MapsRestaurantViewClient.as_view(), name='clientrestaurantlocation'),
    path('clientchurchlocation/', views.MapsChurchViewClient.as_view(), name='clientchurchlocation'),
    # path('exporttemplate', views.export_template, name='export')
    # path('emailmessage/', views.email_message, name='emailmessage')
]

