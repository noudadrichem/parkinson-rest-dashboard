import time
import requests
import random
import threading

def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def uploadData():
    dict_GY521 = {
        'aantaltrillingen': random.randint(1, 100),
        'patientid': 1
    }

    dict_STM32AVR = {
        'staje': bool(random.getrandbits(1)),
        'patientid': 1
    }

    dict_DHT11 = {
    'luchtvochtigheid': random.randint(10, 30),
    'patientid': 1
    }

    print(dict_GY521)
    print(dict_STM32AVR)
    print(dict_DHT11)

    APIURL = 'http://nontwikkel.nl:9094'
    trillingenresponse = requests.post("{}/measurements/add".format(APIURL), json=dict_GY521)
    activiteitenresponse = requests.post("{}/activities/add".format(APIURL), json=dict_STM32AVR)
    dampeningresponse = requests.post("{}/dampening/add".format(APIURL), json=dict_DHT11)

    print({
        'trillingenresponse': trillingenresponse,
        'activiteitenresponse': activiteitenresponse,
        'dampeningresponse': dampeningresponse
    })

setInterval(uploadData, 5)
