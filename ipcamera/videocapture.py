# author: Andre Alves
# -*- coding: utf-8 -*-

import threading
import cv2


class ImprovedVideoCapture:
    def __init__(self, stream):
        self.video_stream = cv2.VideoCapture(stream)
        self.was_read, self.frame = self.video_stream.read()
        self.lock = threading.Lock()
        self.active = False

    def start(self):
        if not(self.active):   
            self.thread = threading.Thread(target=self.readFrames, args=())
            self.active = True
            self.thread.start()
            
    def readFrames(self):
        while self.active:
            was_read, frame = self.video_stream.read()
            with self.lock:
                self.was_read = was_read
                self.frame = frame

    def read(self):
        with self.lock:
            was_read = self.was_read
            frame = self.frame.copy()
        return was_read, frame

    def stop(self):
        self.active = False
        self.thread.join()
        self.video_stream.release()

    def __exit__(self, exec_type, exc_value, traceback):
        self.stop()