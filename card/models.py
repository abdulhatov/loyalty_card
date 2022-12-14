from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from django.db import models
from .source.source import STATUS_CARD

class Card(models.Model):
    series = models.BigIntegerField()
    number = models.BigIntegerField()
    release_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    expiration_date = models.DateTimeField(default=datetime.now()+timedelta(days=547))
    date_use = models.CharField(max_length=50, default=str((datetime.now() + timedelta(days=547))-datetime.now()))
    total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    status = models.CharField(max_length=50, choices=STATUS_CARD, blank=True)

    def __str__(self):
        return str(self.number)

