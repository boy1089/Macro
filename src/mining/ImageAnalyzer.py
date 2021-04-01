import cv2
import numpy as np

class ImageAnalyzer :

    def __init__(self):
        self.img = np.zeros([1, 1, 3])
        self.img_processed = np.zeros([1, 1, 3])
        pass

    def getImage(self, img):
        self.img = img

    def img(self):
        print('retuning img')
        return self.img_processed

    def findContours(self):

        img_gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        print('1')
        ret, thresh = cv2.threshold(img_gray, 127, 255,0)
        print('2')
        contours,hierarchy = cv2.findContours(thresh,2,1)
        print('3')
        cnt = contours[0]
        print('4')
        # hull = cv2.convexHull(cnt,returnPoints = False)
        # defects = cv2.convexityDefects(cnt,hull)
        #
        # for i in range(defects.shape[0]):
        #     print(i)
        #     start = tuple(cnt[s][0])
        #     end = tuple(cnt[e][0])
        #     far = tuple(cnt[f][0])
        #     cv2.line(img_gray,start,end,[0,255,0],2)
        #     cv2.circle(img_gray,far,5,[0,0,255],-1  )
        # # print('6')
        self.img_processed = np.asarray(img_gray)
        print('7')
        print(self.img_processed)


    def doThresholding(self):
        pass

    def doCannyEdgeDetection(self):
        pass
