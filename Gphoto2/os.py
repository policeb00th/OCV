import os,subprocess,signal,time
import gphoto2 as gp
camera=gp.Camera()
context=gp.Context()

def kill():
    p=subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
    out,err=p.communicate()

    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid=int(line.split(None,1)[0])
            os.kill(pid,signal.SIGKILL)
kill()
os.system("gphoto2 --set-config /main/capturesettings/capturemode=1")
os.system(" gphoto2 --set-config /main/settings/capturetarget=0")
os.system("gphoto2 --set-config /main/capturesettings/burstnumber=2")
while True:
    os.system("gphoto2 --capture-image-and-download -I 1")

