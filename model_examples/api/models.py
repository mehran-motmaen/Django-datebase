from django.db import models


# Create your models here.
class Simple(models.Model):
    text = models.CharField(max_length=10)
    numbers = models.IntegerField(null=True)
    url = models.URLField(default='example.com')

    def __str__(self):
        return self.url


class DateExample(models.Model):
    the_date = models.DateTimeField()


class Language(models.Model):
    name = models.CharField(max_length=10)


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
