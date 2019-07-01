# author: Andre Alves
# -*- coding: utf-8 -*-

from videocapture import ImprovedVideoCapture


class IpCamera:
    def __init__(self, ip, port=8080, width=640, height=480):
        self.ip = ip
        self.port = port
        self.video_stream = ImprovedVideoCapture(f'http://{self.ip}:{self.port}/video', width, height)
        
    def start(self, silent=False):
        if not(silent):
            if self.video_stream.active:
                print("IpCamera is already running!")
            else:
                print("IpCamera is now running!")
        self.video_stream.start()
         
    def read(self):
        return self.video_stream.read()
    
    def stop(self, silent=False):
        if not(silent):
            print("IpCamera stopped!")
        self.video_stream.stop()