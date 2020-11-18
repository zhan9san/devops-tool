from django.db import models

from applications.models import Application
from environments.models import Environment
from public.models import CommonInfo


class DeploymentBase(CommonInfo):
    env = models.ForeignKey(Environment, blank=False, null=False,
                            on_delete=models.CASCADE)

    app = models.ForeignKey(Application, blank=False, null=False,
                            on_delete=models.CASCADE)

    package = models.CharField(max_length=200)
    ticket = models.CharField(max_length=20, blank=True, null=True)
    jenkins_build_url = models.URLField(max_length=200, blank=True, null=True,)

    class Meta:
        abstract = True


class CurrentPackage(DeploymentBase):
    pass


class Deployment(DeploymentBase):
    def save(self, *args, **kwargs):
        defaults = {
            'name': self.name,
            'package': self.package,
            'ticket': self.ticket,
            'jenkins_build_url': self.jenkins_build_url,
        }

        current_package, _ = CurrentPackage.objects.update_or_create(
            env=self.env,
            project=self.project,
            app=self.app,
            defaults=defaults)

        current_package.save()

        super().save(*args, **kwargs)
