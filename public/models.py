from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    description = models.CharField(max_length=100,
                                   blank=True,
                                   null=True)
    change_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('-change_date',)
