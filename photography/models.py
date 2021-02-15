from django.db import models
from django.urls import reverse
import re

# Generate Models for Ryerson Events
class RyersonEvent(models.Model):
    title = models.CharField(max_length=255)
    event_date = models.DateField()

    def __str__(self):
        return self.title

    def get_all_images(self):
        return RyersonEventImage.objects.filter(post=self)

    class Meta:
        verbose_name_plural = "Ryerson Events"
    
class RyersonEventImage(models.Model):
    post = models.ForeignKey(RyersonEvent, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/photography/events/ryerson-events/')

    def __str__(self):
        return "Ryerson Event"

# Generate Models for TCE
class TCEModel(models.Model):
    title = models.CharField(max_length=255, default="TCE")

    def __str__(self):
        return "TCE"

    def get_all_images(self):
        return TCEImage.objects.filter(post=self)

    class Meta:
        verbose_name_plural = "TCE"

class TCEImage(models.Model):
    post = models.ForeignKey(TCEModel, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/photography/events/tce/')

    def __str__(self):
        return "TCE Image"

# Generate Models of Creative
class Creative(models.Model):
    project_title = models.CharField(max_length=255)
    project_thumbnail = models.ImageField(upload_to='images/photography/creative/project-thumbnails/', default=None)
    slug = models.SlugField(null=False, unique=True)

    def get_matchname(self):
        return re.sub("\W+" , "", self.project_title.lower()) 

    def __str__(self):
        return self.get_matchname()

    def get_all_images(self):
        return ProjectImage.objects.filter(post=self)

    def get_absolute_url(self):
            return reverse('project', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Projects"

class ProjectImage(models.Model):
    post = models.ForeignKey(Creative, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/photography/creative/projects/')

    def __str__(self):
        return "Project Image"