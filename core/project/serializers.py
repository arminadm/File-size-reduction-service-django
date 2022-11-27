from rest_framework import serializers
from .models import UploadedFiles

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFiles