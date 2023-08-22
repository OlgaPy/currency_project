from django.db import models


class Currency(models.Model):
    """
    Model representing a currency.
    """
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        """
        Returns the string representation of the currency.
        """
        return self.code


class RateSource(models.Model):
    """
    Model representing a rate source.
    """
    code = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        """
        Returns the string representation of the rate source.
        """
        return self.code


class CurrencyRate(models.Model):
    """
    Model representing a currency rate.
    """
    date = models.DateField()
    rate_source = models.ForeignKey(RateSource, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Returns the string representation of the currency rate.
        """
        return f"{self.currency} - {self.rate} ({self.rate_source})"
