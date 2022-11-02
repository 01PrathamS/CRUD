from django.db import models  

# create a User model to save information in the database
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

    