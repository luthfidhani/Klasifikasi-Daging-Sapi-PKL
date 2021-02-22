import numpy as np

def contrast(glcm):
    cont = 0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            cont += (i-j)**2 * glcm[i,j] 

    return cont

def diss(glcm):
    diss =0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            diss += glcm[i,j] * np.abs(i-j)
    return diss

def homog(glcm):
    homo = 0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            homo += glcm[i,j] / (1.+(i-j)**2)
    return homo

def asm(glcm):
    asm =0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            asm  += glcm[i,j]**2
    return asm

def corr(glcm):
    corr = 0 
    xbari = 0
    xbarj = 0
    sigi = 0
    sigj = 0
    x1 = 0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            xbari += glcm[i,j] * i
            xbarj += j * glcm[i,j]
            sigi += glcm[i,j]*(i-xbari)**2
            sigj += glcm[i,j]*(j-xbarj)**2
            x1 += ((i-xbari)*(j-xbarj))*glcm[i,j]
    corr = (x1/np.sqrt(sigi*sigj))
    return corr


def energy(glcm):
    energy =0
    asm =0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            asm  += glcm[i,j]**2
    energy = np.sqrt(asm)
    return energy

def entro(glcm):
    entro1 =0
    for i in range(len(glcm)):
        for j in range(len(glcm)):
            entro1  += glcm[i,j]
    entro = np.log(entro1)* entro1
    return entro
