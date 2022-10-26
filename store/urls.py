from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreView.index, name='store_index'),
]
