from django.urls import path
from .views import IncomeView, TotalIncomeView

urlpatterns = [
    path('record/', IncomeView.as_view(), name='record'),
    path('total/',TotalIncomeView.as_view(),name='total'),
]