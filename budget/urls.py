from django.urls import path
from . import views

urlpatterns = [
    path('sandbox', views.SandboxView.index, name='sandbox_index'),
]
