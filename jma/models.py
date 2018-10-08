from django.db import models


# AreaInformationCity.
class AreaInformationCity(models.Model):
    code = models.CharField(verbose_name='市区町村コード', max_length=7, )
    name = models.CharField(verbose_name='市区町村名', max_length=20, )
    lon = models.CharField(verbose_name='経度', max_length=10, null=True, blank=True, )
    lat = models.CharField(verbose_name='緯度', max_length=10, null=True, blank=True, )

    def __str__(self):
        return self.code + ":" + self.name


class Earthquake(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(verbose_name='UUID', max_length=40, )
    date = models.DateTimeField(verbose_name='発生日時')
    maxint = models.CharField(verbose_name='最大震度', max_length=1,  null=True, blank=True, )
    epicenter = models.CharField(verbose_name='震源地', max_length=10,  null=True, blank=True, )
    center_lon = models.CharField(verbose_name='震源地経度', max_length=7,  null=True, blank=True, )
    center_lat = models.CharField(verbose_name='震源地緯度', max_length=7,  null=True, blank=True, )
    upddt = models.DateTimeField(verbose_name='更新日時',  null=True, blank=True, )

    def __str__(self):
        return self.uuid


class EarthquakeDetail(models.Model):
    uuid = models.ForeignKey(Earthquake, on_delete=models.CASCADE)
    intensity = models.CharField(verbose_name='震度', max_length=3, )
    citycode = models.CharField(verbose_name='市区町村コード', max_length=7, )

    def __str__(self):
        return self.citycode + ":" + self.intensity
