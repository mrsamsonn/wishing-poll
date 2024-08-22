from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_poll, name='redirect_to_poll'),
    path('<int:poll_id>/', views.poll_view, name='poll_view'),
    path('vote/', views.vote, name='vote'),
    path('<int:poll_id>/data/', views.get_poll_data, name='get_poll_data'),
    path('<int:poll_id>/add_option/', views.add_option, name='add_option'),
    # path('<int:poll_id>/edit/', views.edit_poll, name='edit_poll'),
]
