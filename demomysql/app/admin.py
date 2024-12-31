from django.contrib import admin
from .models import *
# Register your models here.

#changes is admin pannel to show data
class DemodataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')


admin.site.register(Demodata, DemodataAdmin)