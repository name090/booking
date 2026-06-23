from django.contrib import admin
from .models import Category, Apartments, Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'apartment', 'check_in', 'check_out', 'user', 'created_at')
    list_filter = ('apartment', 'check_in', 'check_out', 'created_at')
    search_fields = ('name', 'email', 'phone', 'apartment__name')
    
admin.site.register(Category)
admin.site.register(Apartments)
admin.site.register(Booking)