from django.contrib import admin

from .models import History, LatestPackage


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'env', 'project', 'app', 'package', 'ticket', 'jenkins_build_url')


class LatestPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'env', 'project', 'app', 'package', 'ticket', 'jenkins_build_url')


admin.site.register(History, HistoryAdmin)
admin.site.register(LatestPackage, LatestPackageAdmin)
