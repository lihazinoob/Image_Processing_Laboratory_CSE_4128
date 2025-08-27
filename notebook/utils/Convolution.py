import numpy as np
import cv2
import sys

def Convolution(image,kernel,anchor_row,anchor_col):
  height,width = image.shape
  kernel_height,kernel_width = kernel.shape
  
  # Now we need to flip the kernel
  # flipped_kernel = flip_kernel(kernel)
  
  # Padding calculation
  pad_top = anchor_row
  pad_bottom = kernel_height -anchor_row -1
  pad_left = anchor_col
  pad_right = kernel_width - anchor_col - 1
  
  padded_image = cv2.copyMakeBorder(image, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_REPLICATE)
 
  
  
  #  Output image
  output_image = np.zeros((height, width), dtype=np.float32)
  
  
  # Do the convolution
  for v in range(height):
    for u in range(width):
      total = 0.0
      for j in range(kernel_height):
        for i in range(kernel_width):
          y = v + j 
          x = u + i 
          kernel_y = kernel_height - 1 - j
          kernel_x = kernel_width - 1 - i
          total += padded_image[y,x] * kernel[kernel_y, kernel_x]
      
      output_image[v,u] = total
      
  normed_image = np.round(cv2.normalize(output_image, None, 0, 255, cv2.NORM_MINMAX)).astype(np.uint8)    
  return normed_image