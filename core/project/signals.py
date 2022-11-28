from django.dispatch import receiver
from django.db.models.signals import post_save
from .task import convert_video
from .models import UploadedFiles

@receiver(post_save, sender=UploadedFiles)
def start_convert(sender, instance, created, **kwargs):
    if created:
        convert_video.delay(instance.video_org.name, instance.id)