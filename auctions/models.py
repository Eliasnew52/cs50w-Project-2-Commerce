from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    pass

class Category(models.Model):
    CatName= models.CharField(max_length=40)
    
    def __str__(self):
        return self.CatName


class Listings(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=300)
    Image = CloudinaryField('image')
    Price = models.FloatField()
    IsActive = models.BooleanField(default = True)
    Owner = models.ForeignKey(User,on_delete=models.CASCADE, blank = True, null = True, related_name = 'user')
    Item_Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, related_name = 'category')

    Watchlist = models.ManyToManyField(User,blank=True,null=True,related_name="watchlist")

    def __str__(self):
        return self.Title


class Comments(models.Model):
    Author= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='author_comment')
    Listing= models.ForeignKey(Listings,on_delete=models.CASCADE, blank=True,null=True,related_name='listing_comment')
    Comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.Author} comment on {self.Listing}"

class Bid(models.Model):
    BidCreator = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='bid_creator')
    BidListing = models.ForeignKey(Listings,on_delete=models.CASCADE,blank=True,null=True,related_name='bid_listing')
    BidAmount = models.FloatField()

    def __str__(self):
        return f"{self.BidCreator}'s Bid of {self.BidAmount} on {self.BidListing}"