from django.contrib import admin
from .models import Category, Offer

admin.site.site_header = "INSERT Advertisments API"
admin.site.site_title = "Advertisments CRUD API"
admin.site.index_title = "Manage Advertisment API"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ('name',)
    list_filter = ['name', ]
    # list_editable = ('name')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'created_at', 'category']
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'price')
