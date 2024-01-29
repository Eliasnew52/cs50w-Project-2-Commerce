from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    pass

class Category(models.Model):
    CatName= models.CharField(max_length=40)


class Listings(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=300)
    Image = CloudinaryField('image')
    Price = models.FloatField()
    IsActive = models.BooleanField(default = True)
    Owner = models.ForeignKey(User,on_delete=models.CASCADE, blank = True, null = True, related_name = 'user')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, related_name = 'category')