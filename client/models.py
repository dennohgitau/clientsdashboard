from django.db import models

# Create your models here.
class Client(models.Model):
    created_at = models.CharField(max_length=256)
    order_no = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    client_phone = models.BigIntegerField()
    client_address = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    delivery_status = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    delivery_date = models.DateField()
    total_price = models.FloatField()
    confirmed = models.CharField(max_length=256)



     
