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
                                       cv2.THRESH_BINARY,51,2)
        contours,hierarchy = cv2.findContours(thresh,2,1)

        contours_large = [x for x in contours if cv2.contourArea(x)> 1000]
        print('# of contours : ', len(contours_large))
        # contours_2 = [x for x in contours_large if cv2.contourAspect]
        for j in range(len(contours_large)):
            cnt = contours_large[j]

            cv2.drawContours(self.img, cnt, -1, (0, 255, 0), 3)
            print(cv2.contourArea(cnt))
        self.img_processed = np.asarray(self.img)
        self.img_inline = thresh


    def doThresholding(self):
        pass

    def doCannyEdgeDetection(self):
        pass
