from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    phtoto = models.ImageField(upload_to='fotos/',null=False, blank=False)