from django.db import models

# Create your models here.
class products(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category_id=models.IntegerField()
    # rating=models.DecimalField(max_digits=2,decimal_places=1)

class Rating(models.Model):
    rate=models.DecimalField(max_digits=2,decimal_places=1)
    count=models.ImageField()


class order(models.Model):
    id=models.IntegerField(primary_key=True)
    products=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField()
    status=models.CharField(max_length=200)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2)
