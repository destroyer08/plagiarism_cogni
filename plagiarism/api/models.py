from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Key(models.Model):
    key = models.TextField(max_length=20, primary_key=True, unique=True)

    def __unicode__(self):
        return self.key

