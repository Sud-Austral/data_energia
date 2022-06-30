import requests as req
import json
import pandas as pd
import sys

#BENCINA EN LÍNEA:

def proceso():
    url = 'https://3b9x.short.gy/xAW5bI'
    file = req.get(url, allow_redirects=True)
    open('data.csv', 'wb').write(file.content)
    return
    






if __name__ == '__main__':
    proceso()
    
