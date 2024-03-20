from cv2.typing import MatLike
import numpy as np
import math

def high_pass_filter(image:MatLike, r:int) -> MatLike:
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 0
    return mask

def low_pass_filter(image:MatLike, r:int) -> MatLike:
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros((rows, cols), np.uint8)
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 1
    return mask

def butterworth_high_pass_filter(image: np.ndarray, r: int, n: int) -> np.ndarray:
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    
    u, v = np.meshgrid(np.arange(-ccol, cols - ccol), np.arange(-crow, rows - crow))
    d_squared = u**2 + v**2
    d_squared[crow, ccol] = 1  # Avoid division by zero at the center
    mask = 1 / (1 + (r / d_squared)**(2*n))
    return mask

def butterworth_low_pass_filter(image: np.ndarray, r: int, n: int) -> np.ndarray:
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    
    u, v = np.meshgrid(np.arange(-ccol, cols - ccol), np.arange(-crow, rows - crow))
    d_squared = u**2 + v**2
    d_squared[crow, ccol] = 1  # Avoid division by zero at the center
    mask = 1-(1 / (1 + (r / d_squared)**(2*n)))
    return mask