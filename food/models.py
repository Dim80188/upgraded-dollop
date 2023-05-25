from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name


class Product(models.Model):
    # создаю абстрактную модель
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    proteins = models.DecimalField(max_digits = 5, decimal_places = 2)
    fats = models.DecimalField(max_digits = 5, decimal_places = 2)
    carbons = models.DecimalField(max_digits = 5, decimal_places = 2)
    vitamin_a = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b1 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b2 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b4 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b5 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b6 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b9 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_b12 = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_c = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_d = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_e = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_h = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_k = models.DecimalField(max_digits = 6, decimal_places = 3)
    vitamin_pp = models.DecimalField(max_digits = 5, decimal_places = 2)
    potassium = models.DecimalField(max_digits = 5, decimal_places = 2)
    calcium = models.DecimalField(max_digits = 5, decimal_places = 2)
    magnesium = models.DecimalField(max_digits = 5, decimal_places = 2)
    sodium = models.DecimalField(max_digits = 5, decimal_places = 2)
    phosphorus = models.DecimalField(max_digits = 5, decimal_places = 2)
    iron = models.DecimalField(max_digits = 5, decimal_places = 2)
    iodine = models.DecimalField(max_digits = 5, decimal_places = 2)
    manganese = models.DecimalField(max_digits = 6, decimal_places = 3)
    copper = models.DecimalField(max_digits = 5, decimal_places = 2)
    selenium = models.DecimalField(max_digits = 5, decimal_places = 2)
    fluorine = models.DecimalField(max_digits = 5, decimal_places = 2)
    chromium = models.DecimalField(max_digits = 5, decimal_places = 2)
    zinc = models.DecimalField(max_digits = 5, decimal_places = 2)
    arginine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    valine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    histidine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    isoleucine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    leucine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    lysine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    methionine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    threonine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    tryptophan = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    phenylalanine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    alanine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    aspartic_acid = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    hydroxyproline = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    glycine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    glutamic_acid = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    proline = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    serene = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    tyrosine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)
    cysteine = models.DecimalField(max_digits = 6, decimal_places = 3, blank=True)

    class Meta:
        abstract = True


    def __str__(self):
        return self.name

class ProductDescription(Product):
    # описывает каждый продукт
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

class Meal(Product):
    # описывает каждый прием пищи конкретного пользователя
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, related_name='user_related', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    event_time = models.DateTimeField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
