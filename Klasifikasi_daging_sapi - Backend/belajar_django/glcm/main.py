import numpy as np
import matplotlib.pyplot as plt
import cv2
from . import croping , glcmat , extraction
import os
from PIL import Image 

def main():
    np.set_printoptions(threshold=np.inf)
    base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    files_dir = os.path.abspath(os.path.join(base_dir, '../../grade5.jpg'))
    img = Image.open(files_dir)
    crop = croping.cropIm(img)
    #(crop = data image sudah diprepro, 1 = jarak antar pixel yang bertetangga, 0 = derajat arah tetangga pixel)
    matrix = glcmat.createMat(crop,1,0)
    #print(matrix)
    con = extraction.contrast(matrix)
    diss = extraction.diss(matrix)
    cor = extraction.corr(matrix)
    energ = extraction.energy(matrix)
    homo = extraction.homog(matrix)
    entr = extraction.entro(matrix)

    glcm = {
        'Contrast' : con,
        'Dissimilarity' :  diss,
        'Correlation' : cor,
        'Energy' :  energ,
        'Homogenity' : homo,
        'Entropy' : entr,
    }

    return glcm