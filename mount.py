#!/usr/bin/python
import os,time
def mount(volume,server_ip,version):

         os.environ['server_ip']=server_ip
         os.environ['volume']=volume
         os.environ['version']=version
         if volume == "ganesha-test-volume" :
                if os.path.isdir('/mnt/ganesha-mnt')==False:
                        os.mkdir('/mnt/ganesha-mnt')
                print "=================Mount ganesha-test-volume on the client in version %s===============" %version
                os.system('mount -t nfs -o vers=$version $server_ip:/ganesha-test-volume  /mnt/ganesha-mnt')

         else:
                if os.path.isdir('/mnt/pynfs-mnt')==False:
                        os.mkdir('/mnt/pynfs-mnt')
                print "=================Mount pynfs-test-volume on the client in version %s==================" %version
                os.system('mount -t nfs -o vers=4 $server_ip:/pynfs-test-volume  /mnt/pynfs-mnt')
                time.sleep(1)

