# author: Andre Alves
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import ConnectionError

from ipcamera.videocapture import ImprovedVideoCapture
from ipcamera.parameters import valid_parameters

# Stream inactivo da bug implementar check
class IpCamera:
    def __init__(self, ip, port=8080, **kwargs):
        self.url = f'http://{ip}:{port}'
        self.video_stream = ImprovedVideoCapture(f'{self.url}/video')
        
        for parameter in kwargs:
            try:
                self.setParameter(parameter, kwargs[parameter])
            except ValueError:
                print(f'Parameter {parameter} was ignored. (Was invalid)')
            except ConnectionError:
                print(f'Connection error while updating parameter {parameter}.')
                
                
    def setParameter(self, parameter, newValue):
        if not(parameter in valid_parameters and newValue in valid_parameters[parameter]):
            raise ValueError('Invalid parameter or value.')     
        try:
            if parameter == 'flashlight':
                command = 'enabletorch' if newValue == 'on' else 'disabletorch'
                response = requests.get(f'{self.url}/settings/{command}', timeout=5)
            else:
                response = requests.get(f'{self.url}/settings/{parameter}?set={newValue}', timeout=5)
            
            response.raise_for_status()
        except:
            raise ConnectionError('IpCamera connection not working.')
    
    
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
