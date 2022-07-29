from django.db import models


class Promise(models.Model):
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    short_link = models.CharField(max_length=200)

    def __str__(self):
        return self.email