from django.contrib import admin
from .models import ToDo

admin.AdminSite.site_header = 'Администрация'
admin.AdminSite.site_title = 'Добро пожаловать'
admin.AdminSite.index_title = 'Добро пожаловать'
admin.AdminSite.empty_value_display = '-пусто-'


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_complete']
