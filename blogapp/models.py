from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_data = models.DateTimeField()
    body = RichTextUploadingField()

    def __str__(self):
        return self.title