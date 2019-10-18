from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Account(models.Model):
    AccountNumber=models.CharField(max_length=10)
    name=models.CharField(max_length=200)
    phoneNumber=models.CharField(max_length=12)
    Balance=models.IntegerField(default=0)

    def __str__(self):
        return self.AccountNumber + ' - ' + self.name
class ATMCard(models.Model):
    ATMCardNumber=models.CharField(max_length=200)
    AccountNumber=models.ForeignKey(Account,on_delete=models.CASCADE)
    PIN=models.IntegerField(default=0)
    name=models.CharField(max_length=200)
    DOI=models.DateField("Date Issued: ")
    ExpirationDate=models.DateField()
    Address=models.CharField(max_length=200)

    def __str__(self):
        return self.ATMCardNumber 
    def isssued_recently(self):
        return self.DOI >= timezone.now() - datetime.timedelta(days=1)
    def expired_recently(self):
        return self.ExpirationDate>= timezone.now() - datetime.timedelta(days=1)
