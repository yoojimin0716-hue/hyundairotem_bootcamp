# Computer Vision(opencv : open source Computer vidion 라이브러리 사용)

#pip install opencv-python 또는 
# conda install opencv-python 
import cv2
print(cv2.__version__)  #opencv 버전은 5.0

img1 = cv2.imread('yoojimin.jpeg') #<class 'NoneType'>
print(type(img1))

cv2.imshow('image test',img1)
cv2.waitKey()
cv2.destroyAllWindows()
# print('end')

#다른이름으로 저장 
cv2.imwrite('yoojimin.jpeg', img1)
cv2.imwrite('yoojimin.jpeg',img1,[cv2.IMWRITE_JPEG_QUALITY,2])

#이미지 크기 조정 
img2 = cv2.resize(img1,(300,100),interpolation=cv2.INTER_AREA)
cv2.imwrite('yoojimin3.jpeg',img2)

# 밝기, 상하좌우 회전, 자르기 
