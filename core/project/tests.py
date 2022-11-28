import os    
from django.test import TestCase
from datetime import datetime
from .models import UploadedFiles

class TestFFMPEG(TestCase):
    def setUp(self):
        self.test_video = "./videos/test/input.mp4"

    def test_ffmpeg_integration(self, res=240):
        video_name = "input.mp4"
        out_path = f"./videos/{res}/{video_name}"
        command_str = f"ffmpeg -i {self.test_video} -vf scale={res}:{res} {out_path}"
        result = os.system(command_str)
        self.assertTrue((result == 0) and (out_path == "./videos/240/input.mp4"))
    