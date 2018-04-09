import cv2
#openCV无需知道算法逻辑，无需进行模型训练
'''打开图像'''
img = cv2.imread('./img/meinv.png')

if len(img.shape)==1:
    #转化为numpy数组
    gray = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
else:
    gray = img
#检测器
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(gray,1.01,3)
print(face)
for (x,y,w,h) in face:
    cut_face = cv2.rectangle(img,(x, y), (x+w, y+h),(255,0,0))
#创建窗口
cv2.namedWindow('Image')

#在窗口中显示图像
cv2.imshow('Image',img)

#通过键盘关闭窗口
cv2.waitKey(0)

#释放窗口
cv2.destroyAllWindows()