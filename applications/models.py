from django.db import models

from public.models import CommonInfo


class Application(CommonInfo):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
