from django.urls import path
from .views import UserAccountsView, InvestmentsView

urlpatterns = [
    path('all/', UserAccountsView.as_view(), name='accounts'),
    path('investments/', InvestmentsView.as_view(),name='investments')
]