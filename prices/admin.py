# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Market, Category, Item, Purchase


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'average', 'least_price', 'category1', 'category2')
    list_filter = ('category1', 'category2')
    search_fields = ('name',)

    @admin.display(ordering='average')
    def average(self, item: Item):
        counter = 0
        total = 0
        for purchase in item.purchase_set.all():
            if purchase.quality:
                counter += 1
                total += purchase.price / purchase.quality
        if counter:
            return round(total / counter, 2)
        return 0

    @admin.display(ordering='average')
    def least_price(self, item: Item):
        start_price = 999999999
        least_price = start_price
        for purchase in item.purchase_set.all():
            price_per_unit = purchase.price / purchase.quality
            if price_per_unit < least_price:
                least_price = price_per_unit
        if least_price == start_price:
            least_price = 0
        return round(least_price, 2)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'item', 'price', 'quality', 'market')
    list_filter = ('date', 'item', 'market')
