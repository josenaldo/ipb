from django.contrib import admin

# Register your models here.
from .models import DevilName

# admin.site.register(DevilName)

# Define the admin class
@admin.register(DevilName)
class DevilNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creation_date')
    list_filter = ('name', 'creation_date')
