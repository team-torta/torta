from django.db import models


# AreaInformationCity.
class AreaInformationCity(models.Model):
    code = models.CharField(verbose_name='市区町村コード', max_length=7, )
    name = models.CharField(verbose_name='市区町村名', max_length=20, )
    lon = models.CharField(verbose_name='経度', max_length=10, null=True, blank=True, )
    lat = models.CharField(verbose_name='緯度', max_length=10, null=True, blank=True, )

    def __str__(self):
        return self.code + ":" + self.name

class Eearthquake(models.Model):
    uuid = models.CharField(verbose_name='UUID', max_length=40, )
    code = models.CharField(verbose_name='市区町村コード', max_length=7, )
    intensity = models.CharField(verbose_name='震度', max_length=1, )
    # いつか地震の情報と市区町村震度を親子テーブルに分ける
    # epicenter = models.CharField(verbose_name='震源地', max_length=10, )
    # date = models.DateTimeField(verbose_name='発生日時')

    def __str__(self):
        return self.uuid
