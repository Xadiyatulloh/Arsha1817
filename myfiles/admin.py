from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPort(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'comp_name', 'tur', 'date', 'rasm1']
admin.site.register(Portfolio, AdminPort)

class AdminTur(admin.ModelAdmin):
    list_display = ['id', 'nomi']
admin.site.register(Type, AdminTur)

class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id', 'ism', 'email', 'sub', 'text', 'date']
admin.site.register(Murojaat, AdminMurojaat)