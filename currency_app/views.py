from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics

from .models import CurrencyRate
from .serializers import CurrencyRateSerializer


def currency_rates(request: HttpRequest) -> HttpResponse:
    """
    View function for displaying currency rates in a table format.
    """
    rate_source = request.GET.get('rate_source', None)
    rates = CurrencyRate.objects.filter(rate_source=rate_source)
    return render(request, 'currency_rates.html', {'rates': rates})


class CurrencyRateList(generics.ListAPIView):
    """
    View class for retrieving currency rates through a REST API.
    """
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer

    def get_queryset(self):
        queryset = CurrencyRate.objects.all()
        date = self.request.query_params.get('date', None)
        from_date = self.request.query_params.get('from', None)
        to_date = self.request.query_params.get('to', None)
        rate_source = self.request.query_params.get('rate_source', None)
        if date is not None:
            queryset = queryset.filter(date=date)
        if from_date is not None and to_date is not None:
            queryset = queryset.filter(date__range=[from_date, to_date])
        if rate_source is not None:
            queryset = queryset.filter(rate_source=rate_source)
        return queryset
