from django.urls import path

from app1 import views

app_name = 'guests'

urlpatterns = [
    path('', views.GuestsView.as_view(), name='guest_list'),
    path('personalize/', views.CreatePersonalizedInvitationView.as_view(), name='personalized_invitation'),
    path('modifiedinvite/', views.CreatedModifiedInvitationView.as_view(), name='modified_invitation'),
    path('<int:pk>/updateinvite/', views.UpdateInviteView.as_view(), name='update_invite'),
    path('finalinvite/', views.FinalInvitationView.as_view(), name='final_invitation'),
    path('add/', views.CreateGuestsView.as_view(), name='add'),
    path('<int:pk>/update/', views.UpdateGuestsView.as_view(), name='update'),
    path('<int:pk>/delete/', views.delete_location, name='delete'),
    path('<int:pk>/activate/', views.activate_location, name='activate'),
    path('confirmationmessage/', views.confirmation_message, name='confirmation')
]