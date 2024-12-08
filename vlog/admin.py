from django.contrib import admin
from .models import VlogPost

# Register your models here.

@admin.register(VlogPost)
class VlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'description')
    date_hierarchy = 'published_date'
