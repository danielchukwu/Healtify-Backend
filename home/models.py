from django.db import models

# Create your models here.

class Appointment(models.Model):
   name = models.CharField(max_length=200)
   contact = models.BigIntegerField(null=False, blank=False)
   email = models.EmailField(null=True, blank=True)
   feel = models.TextField(null=False, blank=False)

   updated = models.DateTimeField(auto_now_add=True)
   created = models.DateTimeField(auto_now=True)

   class Meta:
      ordering = ['created']
   
   def __str__(self):
      return f"{self.name} - {self.feel}"


class Doctor(models.Model):
   name = models.CharField(max_length=200, null=False, blank=False)
   gender = models.CharField(max_length=200, null=False, blank=False)

   class Meta:
      ordering = ['name']

   def __str__(self):
      return f"{self.name} - {self.gender}"