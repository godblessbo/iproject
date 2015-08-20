from django.db import models
from workspace.models import GroupSpace, UserSpace, User_Group_Relation


class Gathering(models.Model):
    desp = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    startTime = models.DateTimeField(null=True, blank=True)
    endTime = models.DateTimeField(null=True, blank=True)
    place = models.CharField(null=True, max_length=128, blank=True)
    eat = models.CharField(null=True, max_length=128, blank=True)
    sleep = models.CharField(null=True, max_length=128, blank=True)
    budget = models.PositiveIntegerField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    group = models.ForeignKey(GroupSpace)

    def __unicode__(self):
        return u'%s' % self.desp


class JoinState(models.Model):
    isJoin = models.BooleanField(default=False)
    reason = models.TextField(null=True, blank=True)
    upMoney = models.BooleanField(default=False)
    relation_key = models.ForeignKey(User_Group_Relation, default=1)
