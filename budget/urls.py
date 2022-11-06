from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/budget/new', views.BudgetView.budget_new, name='budget_new'),
    # path('budget', views.BudgetView.budget_new, name='budget_update'),
]
