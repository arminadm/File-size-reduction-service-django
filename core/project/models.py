from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .task import convert_video

# Create your models here.
class UploadedFiles(models.Model):
    video_org = models.FileField(null=False, blank=False, upload_to="videos/org/")
    video240 = models.FileField(null=True, blank=True, upload_to="videos/240/")
    video360 = models.FileField(null=True, blank=True, upload_to="videos/360/")
    # time duration for creating video240 and 360 of original video
    duration = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"uploaded file: id={self.id}"
    

@receiver(post_save, sender=UploadedFiles)
def start_convert(sender, instance, created, **kwargs):
    if created:
        convert_video.delay(instance.video_org.name)