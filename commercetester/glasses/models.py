from django.db import models

class Site(models.Model):
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.url

    def was_tested_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Supposition(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    response = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.note
