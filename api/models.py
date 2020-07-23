from django.db import models


class GEOPoint(models.Model):
    """Хранение объектов интереса"""
    name = models.CharField(max_length=120)
    lat = models.IntegerField()
    lng = models.IntegerField()

    def __str__(self):
        return self.name


class File(models.Model):
    """Информация о загружаемых файлах"""
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remark
