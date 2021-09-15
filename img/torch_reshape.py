import cv2
import numpy as np
import torch
import torch.nn as nn
img = cv2.imread('./test.jpg',0)
img = np.array(img,dtype='float32')
img = torch.from_numpy(img.reshape(1,1,img.shape[0],img.shape[1]))
avgPool = nn.AvgPool2d(2)
img = avgPool(img)
img = torch.squeeze(img)
img = img.numpy().astype('uint8')
cv2.imwrite("out.jpg", img)
