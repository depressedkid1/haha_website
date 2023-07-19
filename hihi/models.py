from django.db import models
from django.conf import settings
from django.utils import timezone


class People(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    vk_id = models.CharField(max_length=255,default='404')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(default=timezone.now)
    time_publish = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.time_publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title
