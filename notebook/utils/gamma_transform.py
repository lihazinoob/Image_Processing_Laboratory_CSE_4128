import numpy as np
import cv2
  
def Gamma_Transform(image,gamma):
  image = (image)**gamma
  
  image = np.uint8(image)*255
  return image