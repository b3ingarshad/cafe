from django.db import models

# Create your models here.
class ImageProfile(models.Model):
    images=models.ImageField(upload_to='pro_img',blank=True)

class inputmodel(models.Model):
    inputa=models.IntegerField(default="")
    inputb=models.IntegerField(default="")