from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'change_date', 'add_date', 'status')


admin.site.register(Application, ApplicationAdmin)
