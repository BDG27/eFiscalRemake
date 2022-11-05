from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/loja', views.StoreView.store, name='store_view'),
    path('store', views.StoreView.store_update, name='store_update'),
]
