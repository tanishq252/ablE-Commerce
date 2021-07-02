from django.db import models
from .product import Product
from .customer import Customer
import datetime
from store.middlewares.auth import auth_middleware

class Order(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    q = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=15,default='',blank=True)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id)\
            .order_by('-date')