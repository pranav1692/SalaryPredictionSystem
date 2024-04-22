from django.db import models

# Create your models here.

class save_form_data(models.Model):
    education_type = models.CharField(max_length=50)
    education_level = models.IntegerField(max_length=50)
    years_of_experience = models.CharField(max_length=2)
   