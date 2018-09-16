from django.db import models


# AreaInformationCity.
class AreaInformationCity(models.Model):
    code = models.CharField(verbose_name='市区町村コード', max_length=7, )
    name = models.CharField(verbose_name='市区町村名', max_length=20, )
    lon = models.CharField(verbose_name='経度', max_length=10, null=True, blank=True, )
    lat = models.CharField(verbose_name='緯度', max_length=10, null=True, blank=True, )

    def __str__(self):
        return self.code + ":" + self.name
