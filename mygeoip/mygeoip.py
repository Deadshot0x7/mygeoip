import json
import requests

class mgip:

    def __init__(self, ip):
        self.ip = ip


    def lon(self):
        try:
            url = requests.get(f'http://ip-api.com/json/{self.ip}').json()
            return url['lon']

        except:
            return None    

    def city(self):
        try:
            url = requests.get(f'http://ip-api.com/json/{self.ip}').json()
            return url['city']

        except:
            return None    

    def zip(self):
        try:
            url = requests.get(f'http://ip-api.com/json/{self.ip}').json()
            return url['zip']

        except:
            return None
