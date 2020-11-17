from django.db import models

from applications.models import Application, Project
from environments.models import Environment
from public.models import CommonInfo


class Deployment(CommonInfo):
    env = models.ForeignKey(Environment, blank=False, null=False,
                            on_delete=models.CASCADE)
    project = models.ForeignKey(Project, blank=False, null=False,
                                on_delete=models.CASCADE)
    app = models.ForeignKey(Application, blank=False, null=False,
                            on_delete=models.CASCADE)

    package = models.CharField(max_length=200)
    ticket = models.CharField(max_length=20, blank=True, null=True)
    jenkins_build_url = models.URLField(max_length=200, blank=True, null=True,)

    class Meta:
        abstract = True


class LatestPackage(Deployment):
    pass


class History(Deployment):
    def save(self, *args, **kwargs):
        defaults = {
            'name': self.name,
            'package': self.package,
            'ticket': self.ticket,
            'jenkins_build_url': self.jenkins_build_url,
        }

        latest_package, _ = LatestPackage.objects.update_or_create(
            env=self.env,
            project=self.project,
            app=self.app,
            defaults=defaults)

        latest_package.save()

        super().save(*args, **kwargs)
