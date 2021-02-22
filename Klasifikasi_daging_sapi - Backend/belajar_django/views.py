# from django.shortcuts import render

# from scipy import stats
# from sklearn.metrics import classification_report
# import matplotlib.pyplot as plt
from django.http import HttpResponse
import base64
import json
from http import HTTPStatus
import numpy as np
#mengabaikan warning pada output biar enak dilihat :v
import warnings
warnings.filterwarnings('ignore')
np.set_printoptions(suppress=True) # biar output gak keluar nilai e (exp)

import os
import socket
import cv2

# from belajar_django.glcm import main
from . import proses

def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")


def index(request):
    files = request.POST['files']
    file_name = request.POST['file_name']
    
    ip()

    imgdata = base64.b64decode(files)
    with open('file_name.jpg', 'wb') as f:
        f.write(imgdata)
    
    eksekusi = proses.Run()


    data = {
        'status': HTTPStatus.OK,
        'message' : eksekusi[0],
    }

    data = json.dumps(data)

    return HttpResponse(data)