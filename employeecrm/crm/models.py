from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)

    email=models.EmailField()

    gender_options=(
        ("male","male"),
        ("female","female"),
        
    )

    gender=models.CharField(max_length=100,choices=gender_options,default="male")

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    date_of_join=models.DateField()

    address=models.TextField()


    picture=models.ImageField(upload_to="employee_images",null=True,blank=True)

    def __str__(self):
        return self.name

        

