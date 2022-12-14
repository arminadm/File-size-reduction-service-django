from django.db import models

# Create your models here.
class UploadedFiles(models.Model):
    video_org = models.FileField(null=False, blank=False, upload_to="videos/org/")
    video240 = models.FileField(null=True, blank=True, upload_to="videos/240/")
    video360 = models.FileField(null=True, blank=True, upload_to="videos/360/")
    duration = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"uploaded file: id={self.id}"
    
