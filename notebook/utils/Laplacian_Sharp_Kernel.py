import numpy as np
def create_laplacian_sharp_filter(kernel_size,sigma_value):
  kernel = np.zeros((kernel_size,kernel_size),dtype=np.float32)
  kernel_height,kernel_width = kernel.shape
  
  
  # finding the center of the kernel
  center_x = kernel_height // 2
  center_y = kernel_width // 2
  
  for x in range(kernel_height):
    for y in range(kernel_width):
      # finding the distance between the center to a particular element
      dx = x - center_x
      dy = y - center_y
      exponential_value = -(dx**2 + dy**2) / (2 * sigma_value**2)
      coefficient_value = (dx**2 + dy**2 - 2*sigma_value**2)/(sigma_value**4)
      value =coefficient_value * np.exp(exponential_value)
      kernel[x,y] = value
  
  #Normalize the kernel
  kernel = kernel - np.mean(kernel)
  # kernel_sum = np.sum(kernel)
  # kernel = kernel / kernel_sum

  return kernel 
  
  