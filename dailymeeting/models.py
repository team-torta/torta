from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
import locale


class Member(models.Model):
    name = models.CharField(verbose_name='名前', max_length=10, )
    name_short = models.CharField(verbose_name='名前(省略)', max_length=2, )

    def __str__(self):
        return self.name


class Day(models.Model):
    day = models.DateField(verbose_name='日付', null=True, )
    message = models.TextField(verbose_name='メッセージ', null=True, )
    image1 = models.ImageField(verbose_name='添付イメージ１',
                               upload_to='images/', null=True, blank=True, )
    thumbnail1 = ImageSpecField(source='image1',
                                processors=[ResizeToFill(300, 250)],
                                format="JPEG",
                                options={'quality': 60})

    image2 = models.ImageField(verbose_name='添付イメージ２',
                               upload_to='images/', null=True, blank=True, )
    thumbnail2 = ImageSpecField(source='image2',
                                processors=[ResizeToFill(300, 250)],
                                format="JPEG",
                                options={'quality': 60})

    def __str__(self):
        return str(self.day)

    def get_day_of_week(self):
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        return self.day.strftime('%a')
