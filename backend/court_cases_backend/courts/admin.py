from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import CustomUser

class UserAdmin(BaseUserAdmin):   
    # отображение
    list_display = ('email', 'name', 'surename', 'is_admin')
    # фильтры справа в админке
    list_filter = ('is_admin',)
    # созданий групп в админке для удобства
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','surename','patronymic')}),
        ('Permissions', {'fields': ('is_admin', 'is_chief')}),
    )

    # поля, которые необходимо заполнить при создании нового пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surename', 'password1', 'password2'),
        }),
    )

    # поиск в админке будет осуществляться по полям
    search_fields = ('email', 'name', 'surename', 'patronymic')
    # сортировка будет по  следующим полям 
    ordering = ('email',)
    filter_horizontal = ()



admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)