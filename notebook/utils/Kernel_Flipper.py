import numpy as np
def flip_kernel(kernel):
  kernel_height,kernel_width = kernel.shape
  flipped_kernel = np.zeros((kernel_height,kernel_width),dtype=kernel.dtype)
  
  for i in range(kernel_height):
    for j in range(kernel_width):
      flipped_kernel[i,j] = kernel[kernel_height-1-i,kernel_width-1-j]
  
  return flipped_kernel