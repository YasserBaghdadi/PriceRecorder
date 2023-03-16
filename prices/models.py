from django.core.validators import MaxValueValidator
from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category1 = models.ForeignKey(Category, on_delete=models.PROTECT)
    category2 = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, related_name='item_set2')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Purchase(models.Model):
    date = models.DateField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    price = models.FloatField()
    quality = models.FloatField()
    market = models.ForeignKey(to=Market, on_delete=models.PROTECT)
