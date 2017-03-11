import cv2
import glob

img=cv2.imread("galaxy.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("galaxy_resized.jpg",resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

images=glob.glob('./sample-images/*.jpg')

for image in images:
    print(image)
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows
    cv2.imwrite(image+"_resized.jpg",re)
