from django.urls import path
from .views import CurrencyRateList, currency_rates

urlpatterns = [
    path('currency_rates/', CurrencyRateList.as_view(), name='currency_rate_list'),
    path('admin/currency_rates/', currency_rates, name='admin_currency_rates'),
]