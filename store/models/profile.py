from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Profile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    q = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)

    def reg(self):
        self.save()

    @staticmethod
    def get_profile_customer(customer_id):
        return Profile.objects.filter(customer=customer_id)
