
from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
