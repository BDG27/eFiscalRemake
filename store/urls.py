from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/loja', views.StoreView.loja, name='store_view'),
    path('loja', views.StoreView.loja_update, name='store_update'),
]
