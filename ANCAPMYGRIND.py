import time
import os 
import subprocess
import sys

ts = sys.argv[1]
url = sys.argv[1]

lastTime = 0
def getTime(time):
    m, s = time.split(':')
    return int(m) * 60 + int(s)

#subprocess.Popen(["ancapmygrind"])
subprocess.Popen(["google-chrome", url])


time.sleep(2)
lastTime = 0
for line in open(ts, 'r'):
    if line[0] == '0':
        newTime = getTime(line)
        time.sleep(newTime - lastTime)
        lastTime = newTime
    else:
        subprocess.Popen(["cowsay", '"' + line + '"'])
        subprocess.Popen(["espeak", '"' + line + '"'])
