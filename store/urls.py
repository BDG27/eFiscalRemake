from django.urls import path
from . import views

urlpatterns = [
    path('loja', views.StoreView.loja, name='store_new'),
]
