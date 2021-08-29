from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=200)
    information = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='uploads/info/', default='')

    def __str__(self):
        return self.name

    @staticmethod
    def info_get_all():
        return Info.objects.all()
