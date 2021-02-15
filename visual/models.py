from django.db import models

class Visual(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='images/visual/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Visual"