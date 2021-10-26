import json as j
import requests as r
import time as time
import urllib
from urllib.request import urlopen


def findlan(ip):
    url="ttp://ip-api.com/json"+ip

    values=j.load(urlopen(url))
    return(values['lon'])

def findcity(ip):
    url="ttp://ip-api.com/json"+ip

    values=j.load(urlopen(url))
    return(values['city'])

def findcity(ip):
    url="ttp://ip-api.com/json"+ip

    values=j.load(urlopen(url))
    return(values['zip'])


