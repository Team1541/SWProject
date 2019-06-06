import cv2

def binarization(img_cv):
    gray_image_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_image_cv, 127, 255, cv2.THRESH_BINARY)
    gray_image_cv = cv2.bitwise_and(gray_image_cv, gray_image_cv, mask=mask)
    ret, image_cv = cv2.threshold(gray_image_cv, 140, 255, cv2.THRESH_BINARY)
    return image_cv

def cv_resize_maintain_ratio(image,  width = None, height = None):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

def Specific_Valve(img_cv):
    Valve_img = ['./Valve_img/Hand_Manual.JPG','./Valve_img/Globe.JPG']
    Valve_string = ['Hand_Valve', "Globe_Valve"]
    img_cv = binarization(cv_resize_maintain_ratio(img_cv, width=100))
    ret, th = cv2.threshold(img_cv, 127, 255, 0)
    min = 10
    index = -1
    for item in zip(Valve_img, range(0,len(Valve_img)+1)):
        query_path = item[0]
        template_img = cv2.imread(query_path,cv2.IMREAD_COLOR)
        template_img = binarization(cv_resize_maintain_ratio(template_img, width=100))
        param1 = cv2.RETR_CCOMP
        param2 = cv2.CHAIN_APPROX_SIMPLE
        ret, th2 = cv2.threshold(template_img, 127, 255, 0)
        _, contours, hierarchy = cv2.findContours(th, param1,param2)
        cnt1 = contours[0]
        _, contours, hierarchy = cv2.findContours(th2, param1,param2)
        cnt2 = contours[0]
        ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
        if min > ret and ret < 0.1:
            min = ret
            index = item[1]
    if index != -1:
        return Valve_string[index]
    return "Generic"
    #w, h = template_img.shape[::-1]



# Vavle_img = ['Globe valve.JPG', 'Hand (manual).JPG']
# #Vavle_img = ['Globe_Vavle.jpg', 'Hand_Vavle.jpeg']
# Crop_img = "Valve_0.jpg"
# img_cv = cv2.imread(Crop_img,cv2.IMREAD_COLOR)
# img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
# img_cv = cv_resize_maintain_ratio(img_cv,height=100)
# #img_cv = binarization(img_cv)
# detector = cv2.ORB_create()
# sym_key, sym_descriptor = detector.detectAndCompute(img_cv, None)
# bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
# cnt = 0
# for query_path in Vavle_img:
#     query_img = cv2.imread(query_path,cv2.IMREAD_COLOR)
#     query_img = cv_resize_maintain_ratio(query_img,height=100)
#     #query_img = binarization(query_img)
#     query_key, query_descriptor = detector.detectAndCompute(query_img, None)
#     # FLANN_INDEX_KDTREE = 0
#     # index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#     # search_params = dict(checks =50)
#     #
#     # flann = cv2.FlannBasedMatcher(index_params,search_params)
#     # matches = flann.knnMatch(sym_descriptor, query_descriptor, k=2)
#
#     #matches = bf.match(sym_descriptor, query_descriptor)
#     matches = bf.knnMatch(sym_descriptor, query_descriptor, k=2)
#
#     # Sort them in the order of their distance.
#
#     good = []
#     for m, n in matches:
#         if m.distance < 1.0 * n.distance:
#             good.append([m])
#     # Draw first 10 matches.
#
#     img = cv2.drawMatchesKnn(img_cv, sym_key, query_img, query_key, good, None, flags=2)
#     cv2.imwrite("RESULT{}.jpg".format(cnt), img)
#     cnt +=1