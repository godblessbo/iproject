from django.db import models
from django.contrib.auth.models import User


class UserSpace(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    highSchool = models.CharField(max_length=64, null=True, blank=True)
    college = models.CharField(max_length=64, null=True, blank=True)
    qq = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    major = models.CharField(null=True, blank=True, max_length=64)
    company = models.CharField(null=True, blank=True, max_length=64)
    phone = models.CharField(null=True, blank=True, max_length=11)
    homeaddr = models.CharField(null=True, blank=True, max_length=64)
    loginUser = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.name)


class GroupSpace(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    creator = models.CharField(max_length=30, null=True, blank=True)
    createTime = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class User_Group_Relation(models.Model):
    group = models.ForeignKey(GroupSpace)
    user = models.ForeignKey(UserSpace)
    remove = models.BooleanField(default=False)

