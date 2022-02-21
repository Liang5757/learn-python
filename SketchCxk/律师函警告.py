import cv2
import os

# 打开文件
src_file_path = os.getcwd() + os.path.sep + 'src'
cap = cv2.VideoCapture(src_file_path + os.path.sep + 'cxk.flv')

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    # 转灰度图
    img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # 高斯模糊, (5,5)参数就表示高斯核, 核尺寸越大图像越模糊
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # 自适应二值化
    img_threshold1 = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

    # 边线更宽，降噪
    img_threshold1_blurred = cv2.GaussianBlur(img_threshold1, (5, 5), 0)

    # 200表示将图片中像素值为200以上的点都变成255，255就是白色
    _, img_threshold2 = cv2.threshold(img_threshold1_blurred, 200, 255, cv2.THRESH_BINARY)

    # 去掉图片中一些细小的噪点，这种效果可以通过图像的开运算来实现
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # cv2.bitwise_not()，原来是0的像素点变成最大值，原来是最大值的像素点变成0。相当于黑色的地方变成白色，白色的地方变成黑色
    img_opening = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(img_threshold2), cv2.MORPH_OPEN, kernel))

    # 再次高斯模糊
    img_opening_blurred = cv2.GaussianBlur(img_opening, (3, 3), 0)
    cv2.imshow('img_opening_blurred', img_opening_blurred)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
