from django.contrib import admin

# Register your models here.
from core.models import (News, Setting, Category, Product, Contact, Subscriber)
from modeltranslation.admin import TranslationAdmin


admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Subscriber)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'like', 'dislike', 'views',)
    search_fields = ('title', 'content',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('created_at',)
    readonly_fields = ('like', 'dislike', 'views', 'created_at', 'updated_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content','category', 'image','is_active')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('like', 'dislike', 'views', 'created_at', 'updated_at',)
        }),
    )

