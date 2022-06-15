from django.contrib import admin
from .models import rating


class ratingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(rating, ratingAdmin)