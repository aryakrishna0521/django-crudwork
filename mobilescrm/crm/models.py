from django.db import models

# Create your models here.

class Mobile(models.Model):

    name=models.CharField(max_length=100)

    brand=models.CharField(max_length=200)

    price=models.PositiveIntegerField()

    RAM=models.CharField(max_length=100)

    color=models.CharField(max_length=100)

    picture=models.ImageField(upload_to="mobile_images",null=True,blank=True)


def __str__(self):
    return self.name
