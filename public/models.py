from django.db import models


class CommonInfo(models.Model):
    change_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ('-change_date',)
