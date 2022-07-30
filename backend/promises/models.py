from django.db import models
import random
import string

class Promise(models.Model):
    def generate_link():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    pub_date = models.DateTimeField('date published', auto_now_add = True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    short_link = models.CharField(max_length=200, default=generate_link)

    def __str__(self):
        return ','.join([str(self.name), str(self.email), str(self.short_link)])

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')