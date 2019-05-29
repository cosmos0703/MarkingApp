#pylint: disable=no-member
from ..Core import BaseImageProcessor
import numpy
import cv2
import tempfile
import os

class OpenCVImageProcessor(BaseImageProcessor):

    def extract_questions(self, dir: str, file: str):
        #extract image, load in greyscale
        img = cv2.imread(file, 0)
        file_extension = os.path.splitext(file)[1]

        #threshold
        img_bin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 18)
        
        #invert
        img_bin = 255-img_bin

        # Defining a kernel length
        kernel_length = numpy.array(img).shape[1]//80
        
        # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
        verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))

        # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
        hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))

        # A kernel of (3 X 3) ones.
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        # Morphological operation to detect vertical lines from an image
        img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=3)
        verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=3)
        with tempfile.NamedTemporaryFile(dir=dir,suffix=file_extension,delete=False) as tmp:
            cv2.imwrite(tmp.name, verticle_lines_img)

        # Morphological operation to detect horizontal lines from an image
        img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
        horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
        with tempfile.NamedTemporaryFile(dir=dir, suffix=file_extension, delete=False) as tmp:
            cv2.imwrite(tmp.name, horizontal_lines_img)

        # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
        alpha = 0.5
        beta = 1.0 - alpha

        # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
        img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
        img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
        img_final_bin = cv2.adaptiveThreshold(img_final_bin, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 18)

        #save
        with tempfile.NamedTemporaryFile(dir=dir, suffix=file_extension, delete=False) as tmp:
            cv2.imwrite(tmp.name, img_final_bin)