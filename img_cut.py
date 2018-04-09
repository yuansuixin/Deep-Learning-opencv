import cv2
import numpy as np

'''打开图像'''
img = cv2.imread('./img/weimi.png')
img_dog = cv2.imread('./img/dog.jpg')
img_dog = cv2.resize(img_dog,(44,44))
print(img.shape,len(img.shape))
if len(img.shape)==1:
    gray = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
else:
    gray = img
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(img)
print(face)
for (x,y,w,h) in face:
    #(图像对象，圆心，半径，颜色，封闭？)
    #cut_face = img[y:y+w,x:x+h]
    img[y:y + w, x:x + h] = img_dog

#创建窗口
cv2.namedWindow('Image')

#在窗口中显示图像
cv2.imshow('Image',img)

#通过键盘关闭窗口
cv2.waitKey(0)

#释放窗口
cv2.destroyAllWindows()