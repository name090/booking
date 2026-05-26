from django.contrib import admin
from .models import Category, Apartments, Booking

# Register your models here.
admin.site.register(Category)
admin.site.register(Apartments)
admin.site.register(Booking)