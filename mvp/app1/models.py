from django.db import models

from django.urls import reverse

class Alpha(models.Model):
    int_val = models.IntegerField(default=0)
    string_val = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('app1:alpha-update', args=[self.id])

    def __str__(self):
        return "%d:%s" % (self.int_val, self.string_val)

class Beta(models.Model):
    int_val = models.IntegerField(default=0)
    string_val = models.CharField(max_length=20)

    def __str__(self):
        return "%d:%s" % (self.int_val, self.string_val)
