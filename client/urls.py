from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/client/<int:id>', views.ClientView.client, name='client_view'),
    path('client', views.ClientView.client_update, name='client_update'),
]
