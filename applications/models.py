from django.db import models

from public.models import CommonInfo


class Project(CommonInfo):
    pass


class Application(CommonInfo):
    project_name = models.ForeignKey(Project,
                                     blank=False, null=False,
                                     on_delete=models.CASCADE)
