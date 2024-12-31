from django.contrib import admin
from .models import *
# Register your models here.

#changes is admin pannel to show data
class DemodataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email')

    #after creating admin model you can comment this __str__ method


admin.site.register(Demodata, DemodataAdmin)