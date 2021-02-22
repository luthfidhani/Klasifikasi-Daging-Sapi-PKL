import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops
import sys
from skimage import io
import pandas as pd
import glob
from openpyxl import load_workbook
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image 
import os


def DataImage():
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    files_dir = os.path.abspath(os.path.join(base_dir, '../file_name.jpg'))
    image = plt.imread(files_dir)
    return(image)

def DataExcel():
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    files_dir = os.path.abspath(os.path.join(base_dir, '../data.xlsx'))

    dataset = pd.read_excel (files_dir)
    fitur = dataset.iloc[:, :6].values
    kelas = dataset.iloc[:, 6].values
    
    data = {
        'dataset' : dataset,
        'fitur' : fitur,
        'kelas' : kelas,
    }

    return(data)

def Crop (image):
    new_width = 700
    new_height = 700
    height, width, depth = image.shape   # Get dimensions

    startx = width//2-(new_width//2)
    starty = height//2-(new_height//2)    
    crop = image[starty:starty+new_height,startx:startx+new_width]
    return (crop)

def Rgb2Gray(crop):
    gray = crop[:,:,0]
    return(gray)

def Glcm(gray):
    glcm = greycomatrix(gray, [1], [0],  symmetric = True, normed = True )
    contrast = greycoprops(glcm, 'contrast')
    dissimilarityraster = greycoprops(glcm, 'dissimilarity')
    homogeneityraster = greycoprops(glcm, 'homogeneity')
    energyraster = greycoprops(glcm, 'energy')
    correlationraster = greycoprops(glcm, 'correlation')
    ASMraster = greycoprops(glcm, 'ASM')

    glcm = {
        'contrast' : contrast[0,0],
        'dissimilarityraster' : dissimilarityraster[0,0],
        'homogeneityraster' : homogeneityraster[0,0],
        'energyraster' : energyraster[0,0],
        'correlationraster' : correlationraster[0,0],
        'ASMraster' : ASMraster[0,0],
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

    image = DataImage()
    excel = DataExcel()

    crop = Crop(image)
    gray = Rgb2Gray(crop)
    glcm = Glcm(gray)
    
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
    knn = Knn(excel['fitur'], data_train, excel['kelas'], 7)
    print(knn)

    return(knn)