from django.db import models

class Member(models.Model):
    # member_id = models.CharField(verbose_name='メンバーID', max_length=10, )
    member_nm = models.CharField(verbose_name='氏名', max_length=10, )

    def __str__(self):
        return self.member_nm


class Event(models.Model):
    # event_id = models.CharField(verbose_name='イベントID', max_length=10, )
    event_nm = models.CharField(verbose_name='イベント名', max_length=20, )
    date = models.DateTimeField(verbose_name='日時')
    place = models.CharField(verbose_name='場所', max_length=50, null=True, blank=True, )
    participants = models.ManyToManyField(Member, blank=True, )
    # comment = models.TextField(verbose_name='コメント', null=True, blank=True, )

    def __str__(self):
        return self.event_nm

    # def get_participant_no(self):
    #     return Participant.objects.filter(participant__event=self).count()
        # return Event.objects.filter(event__participant=self).count()


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, )

    def __str__(self):
        return str(self.event) + "-" + str(self.member)
