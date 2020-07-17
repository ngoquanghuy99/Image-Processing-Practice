
# coding: utf-8

# In[1]:


import cv2
import numpy as np

img_rgb = cv2.imread('opencv-template-matching-python-tutorial.jpg') # đọc ảnh nguồn
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # chuyển sang ảnh xám

template = cv2.imread('opencv-template-for-matching.jpg',0) # đọc ảnh mẫu
w, h = template.shape[::-1]  # gán giá trị w = rộng, h = độ cao (nhớ là của ảnh mẫu)


# In[2]:


res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)  # dùng để tìm vùng tương đồng,
threshold = 0.8 # khai báo ngưỡng
loc = np.where( res >= threshold) # những chỗ >= ngưỡng


# In[3]:


for pt in zip(*loc[::-1]): # trượt trên những vùng tương đồng
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) # vẽ cái hình chữ nhật

cv2.imshow('Detected',img_rgb) # show ảnh
cv2.waitKey(0)
cv2.destroyAllWindows()

