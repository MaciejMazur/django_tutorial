from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTiemField('date published')

class Choice(models.Model):
    poll = models.ForeigKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
