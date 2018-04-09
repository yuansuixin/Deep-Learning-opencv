
import cv2
# 从摄像头中取得视频
cap = cv2.VideoCapture(0)

# 获取视频播放界面长宽
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

# 指定编码
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#视频的输出格式
out = cv2.VideoWriter('./output.mp4', fourcc, 10, (width, height))

while(cap.isOpened()):
    #读取帧摄像头 ret:返回布尔值   frame：返回每一帧
    ret, frame = cap.read()
    #print(frame.shape)
    if ret == True:
        #翻转每一帧
        resultFrame = cv2.flip(frame,1)
        if len(resultFrame.shape)==1 :
            gray = cv2.cvtColor(resultFrame,cv2.COLOR_BAYER_BG2GRAY)
        else:
            gray = resultFrame
        face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        face = face_cascade.detectMultiScale(gray,1.3,5)
        if len(face)>0:
            li = []
            li = face[0]
            cut = resultFrame[li[1]:li[1]+li[2],li[0]:li[0]+li[3]]
            shp = cut.shape
            img_dog = cv2.imread('./img/dog.jpg')
            img_dog = cv2.resize(img_dog, (shp[0], shp[1]))
            resultFrame[li[1]:li[1] + li[2], li[0]:li[0] + li[3]] = img_dog
        else:
                pass

        out.write(resultFrame)
        cv2.imshow('My Camera',resultFrame)

        #键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break
# 释放资源
out.release()
cap.release()
cv2.destroyAllWindows()

