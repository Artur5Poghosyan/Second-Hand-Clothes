from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    address = models.TextField()

class Garment(models.Model):
    TYPE_CHOICES = [
        ('shirt', 'Shirt'),
        ('jackets', 'Jackets'),
        ('Overcoats', 'overcoats'),
        ('pants', 'Pants'),
        ('dress', 'Dress'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    publisher = models.ForeignKey('User', on_delete=models.CASCADE, related_name='garments')
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.size} - ${self.price}'

