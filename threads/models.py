from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


class Subject(models.Model):

    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads', on_delete=models.DO_NOTHING,)
    subject = models.ForeignKey(Subject, related_name='threads', on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.DO_NOTHING,)
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.comment
