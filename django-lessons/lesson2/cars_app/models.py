from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    model_cars = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}|{self.model_cars}|Price:{self.price}"


