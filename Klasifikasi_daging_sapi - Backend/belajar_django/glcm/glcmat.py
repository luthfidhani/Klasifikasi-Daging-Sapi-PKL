import numpy as np

def createMat(crop, jarak, arah):
    
    img = np.array(crop)
    matrix = np.zeros((256, 256), dtype=int)
    if arah == 0: # 0 derajat
        step = img[jarak:, :] #0
        xstep = img[:-jarak, :] #-0
    elif arah == 45: #45 derajat
        step = img[jarak:, :-jarak] #45
        xstep = img[:-jarak, jarak:] #-45
    elif arah == 90: #90 derajat
        step = img[:, :-jarak] #90
        xstep = img[:, jarak:] #-90
    elif arah == 135: #135 derajat
        step = img[:-jarak, :-jarak] #135
        xstep = img[jarak:, jarak:] #-135
    
    for i, j in zip(step.ravel(), xstep.ravel()):
        matrix[i, j] += 1
        jx = np.sum(matrix)
        

    return (matrix/jx)