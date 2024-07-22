from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'image_display']

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="auto"/>', obj.image.url)
        return "Sin Imagen"
    image_display.short_description = "Imagen"
