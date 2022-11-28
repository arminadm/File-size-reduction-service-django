from redis import Redis, exceptions
from datetime import datetime
from django.test import TestCase
from .models import UploadedFiles
from .task import ffmpeg_covert_progress

class TestFFMPEG(TestCase):
    def setUp(self):
        self.test_video = "./videos/org/input.mp4"
    
    def test_ffmpeg_integration(self, res=240):
        out_path, result = ffmpeg_covert_progress(self.test_video, res)
        self.assertTrue((result == 0) and (out_path == "./videos/240/input.mp4"))

    def test_ffmpeg_full_progress(self):
        # create basic object
        obj = UploadedFiles.objects.create(
            video_org = self.test_video
        )

        # convert video to both 240p and 360p
        start_time = datetime.now()
        out_path1, result1 = ffmpeg_covert_progress(self.test_video, res=240)
        out_path2, result2 = ffmpeg_covert_progress(self.test_video, res=360)
        end_time = datetime.now()
        
        # update obj
        duration = (end_time - start_time).seconds
        obj.duration = duration
        obj.video240 = out_path1
        obj.video360 = out_path2
        obj.save()

        self.assertTrue(
                (result1 == 0) and (result2 == 0) and
                (duration != 0) and (obj.video240 == "./videos/240/input.mp4") and
                (obj.video360 == "./videos/360/input.mp4")
            )
        

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
    