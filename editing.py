import os 
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
from moviepy.editor import *


clip = VideoFileClip("./in_process_video/video_ivyandelder.mp4").set_duration(10)

duration = clip.duration
print("duration :   "+str(duration))

clip0 = clip.subclip(0,2)
freeze_clip = vfx.freeze(clip0,  t=0,freeze_duration= 3 )

clip1_mirror = clip.fx(vfx.time_mirror)


Clip1 = clip.fx( vfx.speedx, 1)

clip2 = clip.subclip(0,6)
clip2_mirror = clip2.fx(vfx.time_mirror)

clip_mirror = clip.fx(vfx.time_mirror)


#reverse video

#output = clip.fx(vfx.time_mirror)
final = concatenate_videoclips([freeze_clip,Clip1, clip_mirror,freeze_clip, clip2, clip2_mirror ], method="compose")
#final_out = vfx.loop(final, duration = 40)
final.write_videofile("./in_process_video/scroll_test_faster123.mp4")

""" .

ffmpeg reader.py
def close(self):
        if self.proc:
            self.proc.terminate()
            self.proc.stdout.close()
            self.proc.stderr.close()
            self.proc.wait()
            self.proc = None
        #if hasattr(self, 'lastread'):
        #    del self.lastread 



  """