from django.urls import path
from .views import IncomeView

urlpatterns = [
    path('record/', IncomeView.as_view(), name='user-income-list'),
]