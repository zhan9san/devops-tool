from django.contrib import admin

from .models import Deployment, CurrentPackage


class DeploymentAdmin(admin.ModelAdmin):
    list_display = ('env', 'app', 'package', 'ticket', 'jenkins_build_url')


class CurrentPackageAdmin(admin.ModelAdmin):
    list_display = ('env', 'app', 'package', 'ticket', 'jenkins_build_url')


admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(CurrentPackage, CurrentPackageAdmin)
