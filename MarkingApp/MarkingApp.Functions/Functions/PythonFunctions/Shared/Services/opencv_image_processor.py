from ..Core import BaseImageProcessor
import numpy
import cv2

class OpenCVImageProcessor(BaseImageProcessor):

    def threshold_and_invert(self, path: str):
        #extract image
        img = cv2.imread(path, 0)

        #threshold
        (thresh, img_bin) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        
        #invert
        img_bin = 255-img_bin

        #save
        cv2.imwrite(path, img_bin)