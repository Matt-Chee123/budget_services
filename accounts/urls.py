from django.urls import path
from .views import UserAccountsView

urlpatterns = [
    path('all/', UserAccountsView.as_view(), name='accounts'),
]