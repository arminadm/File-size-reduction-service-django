from django.contrib import admin
from .models import UploadedFiles

# Register your models here.
class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "video_org",
        "video240",
        "video360",
        "duration",
        "created_date",
        "updated_date",
    ]
    ordering = ["-created_date"]
admin.site.register(UploadedFiles, UploadedFilesAdmin)