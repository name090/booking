from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії номерів'

class Apartments(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    description = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='apartments/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='apartments', verbose_name='Категорія')

    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Апортамент'
        verbose_name_plural = 'Апортаменти'

class Booking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я та прізвище")
    email = models.EmailField(verbose_name='Електронна пошта')
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')

    apartment = models.ForeignKey(Apartments, on_delete=models.CASCADE, related_name='bookings', verbose_name='Апартамент')
    check_in = models.DateField(verbose_name='Дата заїзду')
    check_out = models.DateField(verbose_name='Дата виїзду')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name='Користувач')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення бронювання')

    def __str__(self):
        return f"Бронювання: {self.name} - {self.apartment.name} ({self.check_in} - {self.check_out})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'

