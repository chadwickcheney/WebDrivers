from django.db import models
from django.db.models import IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator
from jsonfield import JSONField

class Site(models.Model):
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')
    num_suppositions = models.IntegerField(
        default=0,
    )
    threat_level = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )

    def __str__(self):
        return self.url

    def was_tested_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Supposition(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    importance = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0),
        ],
    )
    details = models.CharField(max_length=200)
    #steps_to_manifest = JSONField(default=[])
    screenshot = models.ImageField(upload_to="images/", null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.note

class Response(models.Model):
    supposition = models.ForeignKey(Supposition, on_delete=models.CASCADE)
    needs_clarification = models.BooleanField(default=False)
    in_progresss = models.BooleanField(default=False)
    check_again = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)
    note = models.CharField(max_length=200)

    def __str__(self):
        return self.note
