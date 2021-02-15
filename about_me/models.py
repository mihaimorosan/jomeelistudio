from django.db import models

# Generate Models for About Me
class AboutMe(models.Model):
    title = models.CharField(max_length=255, default="About Me")
    image = models.ImageField(upload_to='images/about-me/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About Me"