import subprocess
import thread
import time



# Simple command
def stream_audio(thead,delay):
    while 1==1:
        print "Streamer starting"
        subprocess.call('ffmpeg -i sound.mp3 -f ac3 -strict -2 tcp://localhost:1234?listen', shell=True)
        print "Streamer ends"

def capture_serial(thead,delay):
    "Serial capture starting"
    while 1==1:
        print "checking"
        time.sleep(1)

try:
   thread.start_new_thread( stream_audio, ("Thread-1", 2, ) )
   thread.start_new_thread( capture_serial, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread(s)"
while 1:
   pass

