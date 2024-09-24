from django.contrib import admin

from olcha.models import Category, Group, Product, Image


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('users_like',)


admin.site.register(Image)