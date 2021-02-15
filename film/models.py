from django.db import models
from django.core.validators import FileExtensionValidator

class Movie(models.Model):
    movie_title = models.CharField(max_length=200, null=True)
    movie = models.FileField(upload_to='videos/', null=True, verbose_name="",validators=[FileExtensionValidator(allowed_extensions=['mp4','mov'])])

    def __str__(self):
        return self.movie_title