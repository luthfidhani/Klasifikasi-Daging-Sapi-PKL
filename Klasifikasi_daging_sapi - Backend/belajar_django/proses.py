import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops
# import sys
from skimage import io
import pandas as pd
# import glob
# from openpyxl import load_workbook
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os

def DataImage():
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    files_dir = os.path.abspath(os.path.join(base_dir, '../file_name.jpg'))
    image = plt.imread(files_dir)
    return(image)

def DataExcel(excel_dir):
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    files_dir = os.path.abspath(os.path.join(base_dir, excel_dir))

    dataset = pd.read_excel(files_dir)
    fitur = dataset.iloc[:, :6].values
    kelas = dataset.iloc[:, 6].values

    data = {
        'dataset': dataset,
        'fitur': fitur,
        'kelas': kelas,
    }

    return(data)

def Preprocessing(image):
    # == PREPRO =======================================================================
    # -- Read image -----------------------------------------------------------------------
    img = image
# ----------FIND THE MEAT=======================================================
# convert image dari default opencv (BGR) to RGB
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Penentuan range seleksi warna merah
    lower = np.array([140, 0, 0])
    upper = np.array([255, 115, 115])
# proses masking
    mask = cv2.inRange(image, lower, upper)
# implementasikan mask ke image asli
    resultM = cv2.bitwise_and(image, image, mask=mask)

# operasi closing&opening
    kernel = np.ones((7, 7), np.uint8)
    resultM = cv2.morphologyEx(resultM, cv2.MORPH_CLOSE, kernel)
    resultM = cv2.morphologyEx(resultM, cv2.MORPH_OPEN, kernel)

# Penentuan range seleksi warna merah
    lowerP = np.array([195, 128, 128])
    upperP = np.array([255, 255, 254])
# proses masking
    maskP = cv2.inRange(image, lowerP, upperP)
    resultP = cv2.bitwise_and(image, image, mask=maskP)

# operasi closing&opening
    kernel = np.ones((5, 5), np.uint8)
# resultP = cv.morphologyEx(resultP, cv.MORPH_CLOSE, kernel)
    resultP = cv2.morphologyEx(resultP, cv2.MORPH_OPEN, kernel)

# Disini ada 2 result:

# 1. dimasking dulu baru dilakukan operasi closing&opening
    final_mask = mask + maskP
    result1 = cv2.bitwise_and(image, image, mask=final_mask)
    result2 = cv2.morphologyEx(result1, cv2.MORPH_CLOSE, kernel)
    final_result = cv2.morphologyEx(result2, cv2.MORPH_OPEN, kernel)

    gray = cv2.cvtColor(final_result, cv2.COLOR_BGR2GRAY)

    retval, thresh_gray = cv2.threshold(
        gray, thresh=100, maxval=100, type=cv2.THRESH_BINARY)

# Find object with the biggest bounding box

    points = np.argwhere(gray > 0)
    points = np.fliplr(points)
    x, y, w, h = cv2.boundingRect(points)
    crop = gray[y:y+h, x:x+w]
    crop[crop >= 120] = 255
    crop[crop < 120] = 0

    # cv2.imshow('img', crop)                                   # Display
    # cv2.waitKey()
    return (crop)

def Glcm(gray, neighbors, angel):
    glcm = greycomatrix(gray, [neighbors], [angel],  symmetric=True, normed=True)
    contrast = greycoprops(glcm, 'contrast')
    dissimilarityraster = greycoprops(glcm, 'dissimilarity')
    homogeneityraster = greycoprops(glcm, 'homogeneity')
    energyraster = greycoprops(glcm, 'energy')
    correlationraster = greycoprops(glcm, 'correlation')
    ASMraster = greycoprops(glcm, 'ASM')

    glcm = {
        'contrast': contrast[0, 0],
        'dissimilarityraster': dissimilarityraster[0, 0],
        'homogeneityraster': homogeneityraster[0, 0],
        'energyraster': energyraster[0, 0],
        'correlationraster': correlationraster[0, 0],
        'ASMraster': ASMraster[0, 0],
    }
    return glcm

def Knn(data_train, data_test, kelas_train,  k_value):
    classifier = KNeighborsClassifier(n_neighbors=k_value)
    classifier.fit(data_train, kelas_train)

    kelas_prediksi = classifier.predict(data_test)

    knn = kelas_prediksi
    return(knn)

def Run():
    # image = Data("grade1 (1).png")
    # distance = 4
    # angel = [0, 45, 90, 135]
    distance = 2
    angel = 45
    k = 15
    # for i in range(distance):
    #     i = i+1
    #     for j in angel:
    i = distance
    j = angel
    excel_dir = '../dataset/data('+str(i)+','+str(j)+').xlsx'
    image = DataImage()
    excel = DataExcel(excel_dir)

    reprocessing = Preprocessing(image)
    # gray = Rgb2Gray(reprocessing)
    glcm = Glcm(reprocessing, distance, angel)

    data_train = [
        glcm['contrast'],
        glcm['dissimilarityraster'],
        glcm['homogeneityraster'],
        glcm['energyraster'],
        glcm['correlationraster'],
        glcm['ASMraster']
    ]
    data_train = [data_train]
    # print(excel['fitur'], data_train, excel['kelas'])
    # sys.exit()
    knn = Knn(excel['fitur'], data_train, excel['kelas'], k)
    print('data('+str(i)+','+str(j)+').xlsx '+knn)
    return(knn)
