from django.contrib import admin
from .models import Listings, Category, User
# Register your models here.

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Category)
