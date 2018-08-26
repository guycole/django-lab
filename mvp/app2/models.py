from django.db import models

# Create your models here.

class Gamma(models.Model):
    int_val = models.IntegerField(default=0)
    string_val = models.CharField(max_length=20)

    def __str__(self):
        return "%d:%s" % (self.int_val, self.string_val)

class Delta(models.Model):
    int_val = models.IntegerField(default=0)
    string_val = models.CharField(max_length=20)

    def __str__(self):
        return "%d:%s" % (self.int_val, self.string_val)