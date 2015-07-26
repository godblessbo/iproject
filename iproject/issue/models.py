from django.db import models
from workspace.models import WorkSpace


class Task(models.Model):
    creator = models.CharField(null=True, max_length=50)
    owner = models.CharField(null=True, max_length=50)
    task = models.TextField(null=True)
    process = models.TextField(null=True)
    startTime = models.DateField(null=True)
    endTime = models.DateField(null=True)
    state = models.CharField(default=False, null=True, max_length=10)
    taskspace = models.ForeignKey(WorkSpace, null=True)

    def __unicode__(self):
        return u'%s' % (self.creator)
