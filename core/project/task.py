import os    
from celery import shared_task
from datetime import datetime
from .models import UploadedFiles

def ffmpeg_covert_progress(video_link, res):
    video_name = video_link.split('videos/org/')[1]
    out_path = f"./videos/{res}/{video_name}"
    command_str = f"ffmpeg -i {video_link} -vf scale={res}:{res} {out_path}"
    result = os.system(command_str)
    print(f"##### RESULT : {result} #####")
    return out_path, result

@shared_task
def convert_video(video_link, id):
   # calculate progress duration time
    start_time = datetime.now()
    instance = UploadedFiles.objects.get(id=id)
    
    # generate 240p
    out_path, result = ffmpeg_covert_progress(video_link, 240)
    instance.video240 = out_path

    # generate 360p
    out_path, result = ffmpeg_covert_progress(video_link, 360)
    instance.video360 = out_path

    end_time = datetime.now()
    duration = (end_time - start_time).seconds
    instance.duration = duration

    instance.save()
