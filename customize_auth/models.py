from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    mobile = models.BigIntegerField(unique=True, blank=True)
    birthday = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('created_at', 'name')
