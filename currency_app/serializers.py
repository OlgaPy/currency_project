from rest_framework import serializers

from .models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):
    """
    Serializer class for the CurrencyRate model.
    """

    class Meta:
        model = CurrencyRate
        fields = ['id', 'date', 'rate_source', 'rate', 'currency']
