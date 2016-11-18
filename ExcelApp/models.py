from django.db import models
from django.utils import timezone


class CabDetails(models.Model):
    author = models.ForeignKey('auth.User')
    empId = models.CharField(max_length=200)
    empName = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    tripType = models.CharField(max_length=200)
    rosterDate = models.DateTimeField(blank=True, null=True)
    tripTime = models.CharField(max_length=200)
    locality  = models.CharField(max_length=200)
    cabRegNo = models.CharField(max_length=200)
    cabType = models.CharField(max_length=200)
    cabSerialNo = models.CharField(max_length=200)
    publishDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.empId
