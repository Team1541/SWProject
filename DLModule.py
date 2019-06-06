import demo as Dectection
from PIL import Image, ImageDraw
import pytesseract
import cv2
import numpy as np
import copy
from Valve import Specific_Valve
DEBUG = True
tess_CONFIG = ('--tessdata-dir '"/usr/share/tesseract-ocr/tessdata"' -l eng --oem 3 --psm 3')

def convert_PIL_cv(img, coord, value = 1, resize=None):
    coordinate = copy.deepcopy(coord)
    width = (coordinate[2] - coordinate[0]) / value
    height = (coordinate[3] - coordinate[1]) / value
    coordinate[0] += width
    coordinate[1] += height
    coordinate[2] -= width
    coordinate[3] -= height
    temp = img.crop(coordinate)
    image_cv = np.array(temp)
    image_cv = image_cv[:, :, ::-1].copy()
    if resize is None:
        image_cv = cv2.resize(image_cv, (0, 0), fx=2, fy=2)
    else:
        image_cv = cv2.resize(image_cv, (resize, resize))
    gray_image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_image_cv, 127, 255, cv2.THRESH_BINARY)
    gray_image_cv = cv2.bitwise_and(gray_image_cv, gray_image_cv, mask=mask)
    ret, image_cv = cv2.threshold(gray_image_cv, 140, 255, cv2.THRESH_BINARY)
    return image_cv


def cropSymbol(img, coordinate, value =1):
    width = (coordinate[2] - coordinate[0]) / value
    height = (coordinate[3] - coordinate[1]) / value
    coordinate[0] += width
    coordinate[1] += height
    coordinate[2] -= width
    coordinate[3] -= height
    return img.crop(coordinate)

# def cv_Resize(img_cv, resize=None):
#     if resize is None:
#         return cv2.resize(img_cv, (0, 0), fx=2, fy=2)
#     else:
#         return cv2.resize(img_cv, (resize, resize))

def binarization(img_cv):
    gray_image_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_image_cv, 127, 255, cv2.THRESH_BINARY)
    gray_image_cv = cv2.bitwise_and(gray_image_cv, gray_image_cv, mask=mask)
    ret, image_cv = cv2.threshold(gray_image_cv, 140, 255, cv2.THRESH_BINARY)
    return image_cv

def PIL2CV(img):
    img_cv = np.array(img)
    return img_cv[:, :, ::-1].copy()


# def Feature_matching(img_cv):
#     Vavle_img = ['Globe valve.JPG', 'Hand (manual).JPG']
#     detector = cv2.xfeatures2d.SURF_create(400)
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#     sym_key, sym_descriptor = detector.detectAndCompute(img_cv, None)
#     for query_path in Vavle_img:
#         query_img = cv2.imread(query_path,0)
#         query_key, query_descriptor = detector.detectAndCompute(query_img, None)
#         matches = bf.match(sym_descriptor,query_descriptor)
#         matches = sorted(matches, key=lambda x:x.distance)
#     cv2.compare
#
#     detector.detectAndCompute()
#
#     query_img = Image.open(query_path)
#     query_img_cv = convert_PIL_cv2(query_img)
#     img_cv = convert_PIL_cv2(img)



def main(file_list = ["PID026.JPG"]):
    from time import clock

    predicted_symbols, classes, size = Dectection.main(file_list, DEBUG)

    ret_list = []
    t_start = clock()
    for item in zip(predicted_symbols, file_list):
        keys = item[0].keys()
        img = Image.open(item[1])
        coordinate_list = []
        #draw = ImageDraw.Draw(img)eog
        if 0 in keys:
            for bound in item[0][0]: #Valve
                symbol_dict = {}
                coordinate = bound[0]
                symbol_dict['coord'] = coordinate
                symbol_dict['type'] = 0
                img_cv = PIL2CV(img.crop(coordinate))
                #Feature_matching(img_cv)
                symbol_dict['detail'] = Specific_Valve(img_cv)
                if symbol_dict['detail'] is None:
                    symbol_dict['detail'] = "None"
                coordinate_list.append(symbol_dict)
        if 2 in keys:
            for bound in item[0][2]:
                symbol_dict = {}
                coordinate = bound[0]
                symbol_dict['coord'] = coordinate
                symbol_dict['type'] = 2
                symbol_dict['detail'] = "None"
                coordinate_list.append(symbol_dict)
        if 1 in keys: #
            for bound in item[0][1]:
                symbol_dict = {}
                coordinate = bound[0]
                symbol_dict['coord'] = coordinate
                symbol_dict['type'] = 1
                for i in range(9, 3, -1):
                    temp = []
                    image_cv = convert_PIL_cv(img,coordinate,i)
                    OCR_str = pytesseract.image_to_string(image_cv, config=tess_CONFIG)
                    if len(OCR_str) != 1:
                        OCR_str = OCR_str.replace(' ','').split("\n")
                        temp = _OCR_string(OCR_str[0])
                        if len(OCR_str) != 1:
                            temp += _OCR_digit(OCR_str[1])
                        if len(temp) !=0:

                            break
                symbol_dict['detail'] = temp
                coordinate_list.append(symbol_dict)
        ret_list.append(coordinate_list)
    print("Execution Time : {}".format(clock() - t_start))
    return ret_list, classes
def _OCR_digit(input):
    temp = []
    for item in input:
        if item.isdigit():
            temp.append(item)
    return temp

def _OCR_string(input):
    temp = []
    for item in input:
        if item.isalpha():
            temp.append(item)
    return temp


if __name__ == '__main__':
    main();


