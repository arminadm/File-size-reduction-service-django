from celery import shared_task
from time import sleep
import ffmpeg

@shared_task
def convert_video(video_link):
    video_name = video_link.split('videos/org/')[1]
    # print("##############################################1")
    # stream = ffmpeg.input(video_link)
    # print("##############################################2")
    # stream = ffmpeg.hflip(stream)
    # print("##############################################3")
    # stream = ffmpeg.output(stream, f"videos240{video_name}")
    # print("##############################################4")
    # ffmpeg.run(stream)
    # print("##############################################5")
    # print('#######################################')
    (
        ffmpeg
        .input('input.mp4')
        .hflip()
        .output('output.mp4')
        .run()
    )   
    print(video_name)
    print(video_link)
