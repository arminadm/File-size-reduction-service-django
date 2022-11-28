import os    
from redis import Redis, exceptions
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
    
    def test_ffmpeg_integration(self, res=240):
        video_name = "input.mp4"
        out_path = f"./videos/{res}/{video_name}"
        command_str = f"ffmpeg -i {self.test_video} -vf scale={res}:{res} {out_path}"
        result = os.system(command_str)
        self.assertTrue((result == 0) and (out_path == "./videos/240/input.mp4"))

        
class Test_Redis(TestCase):
    def is_redis_available(self, r):
        try:
            r.ping()
            print("Successfully connected to redis")
        except (exceptions.ConnectionError, ConnectionRefusedError):
            print("Redis connection error!")
            return False
        return True
    
    def test_is_redis_available(self):
        r = Redis(host='localhost',port=6379,db=1)
        self.assertTrue(self.is_redis_available(r))
    