from django.db import models


class WorkSpace(models.Model):
    name = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=10, null=True)
    birth = models.DateField(null=True)
    highSchool = models.TextField(null=True)
    college = models.TextField(null=True)
    qq = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    note = models.TextField(null=True)
