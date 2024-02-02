from django.contrib import admin
from .models import Listings, Category, User, Comments,Bid
# Register your models here.

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Bid)