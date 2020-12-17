from django.db import models

class Service(models.Model):
    service = models.CharField(max_length=100)
    sub_service = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")