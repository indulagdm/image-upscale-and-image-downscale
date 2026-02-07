import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('image_path',0)

im_eye = img[70:100, 120:150]
im_eye2 = img[80:90, 125:140]


downsample1 = cv2.pyrDown(img, (1,1))
upsample1 = cv2.pyrUp(img,(1,1))


plt.subplot(221), plt.imshow(im_eye,'gray')
plt.subplot(222), plt.imshow(im_eye2,'gray')
plt.subplot(223), plt.imshow(upsample1,'gray')
plt.subplot(224), plt.imshow(downsample1,'gray')
plt.show()

[m, n] = img.shape
print('Image Shape Original:', m, n)

[m, n] = im_eye.shape
print('Image Shape of Eye:', m, n)


[m, n] = im_eye2.shape
print('Image Shape of Eye 2:', m, n)


[m, n] = upsample1.shape
print('Image Shape of upsample:', m, n)

[m, n] = downsample1.shape
print('Image Shape of downsample:', m, n)


cv2.imshow('original',img)
cv2.imshow('downsampled',downsample1)
cv2.imshow('upsampled',upsample1)

cv2.waitKey()
cv2.destroyAllWindows()