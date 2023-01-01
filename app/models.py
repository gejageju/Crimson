from django.db import models

# Create your models here.
from datetime import datetime

class Products(models.Model):
    title=models.CharField(max_length=255)
    price=models.IntegerField(default=0)
    url=models.CharField(max_length=255)
    claimed=models.BooleanField(default=False)

class Entry(models.Model):
    name=models.CharField(max_length=255)
    amount=models.IntegerField()
    date = models.DateField((u"Conversation Date"), auto_now_add=True, blank=True)
    time = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True)
class Rewards(models.Model):
    coins=models.IntegerField()