import numpy as np
import cv2
from PIL import Image

def Rotate(images):
    image_rotate = images.transpose(Image.ROTATE_90)
    return(image_rotate)

def cropIm (images):
    new_width = 400
    new_height = 400
    width, height = images.size   # Get dimensions

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im1 = images.crop((left, top, right, bottom))
    
    # Shows the image in image viewer 
    im1.show()
    return (im1)
