# author: Andre Alves
# -*- coding: utf-8 -*-

import cv2

from camera import IpCamera


cam = IpCamera('192.168.1.65')
cam.start(silent=True)

while True:
    _, frame = cam.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.stop()
cv2.destroyAllWindows()