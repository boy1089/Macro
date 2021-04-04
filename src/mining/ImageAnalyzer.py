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
        # ret, thresh = cv2.threshold(img_gray, 127, 255,0)
        thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY,31,2)
        contours,hierarchy = cv2.findContours(thresh,2,1)
        print('# of contours : ', len(contours))
        cnt = contours[0]
        #
        # hull = cv2.convexHull(cnt,returnPoints = False)
        # defects = cv2.convexityDefects(cnt,hull)
        # print(defects.shape[0])
        # for i in range(defects.shape[0]):
        #     print("i: ",   i)
        #     s,e,f,d = defects[i,0]
        #     start = tuple(cnt[s][0])
        #     end = tuple(cnt[e][0])
        #     far = tuple(cnt[f][0])
        #     cv2.line(self.img,start,end,[0,255,0],2)
        #     cv2.circle(self.img,far,5,[0,0,255],-1  )
        cv2.drawContours(self.img, cnt, -1, (0, 255, 0), 3)

        self.img_processed = np.asarray(self.img)


    def doThresholding(self):
        pass

    def doCannyEdgeDetection(self):
        pass
