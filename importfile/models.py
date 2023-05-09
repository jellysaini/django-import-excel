from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Plants(models.Model):
    breed=models.CharField(max_length=120,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.breed
    
    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.created.date()}"


class OrderPlants(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Plants = models.ForeignKey(Plants, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Plants} x{self.count}"

    class Meta:
        verbose_name = 'Order Plant'
        verbose_name_plural = 'Order Plants'