from django.db import models

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    mobile=models.CharField(max_length=50)
    about = models.CharField(default='1', max_length=50)
    address = models.TextField()
    detail = models.TextField()
    prescription = models.TextField()
    visit_date = models.DateTimeField(auto_now_add=True)
    next_visit_date = models.CharField(max_length=150)

    def __str__(self):
        return self.name