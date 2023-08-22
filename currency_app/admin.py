from django.contrib import admin
from .models import Currency, RateSource, CurrencyRate

admin.site.register(Currency)
admin.site.register(RateSource)
admin.site.register(CurrencyRate)
