import cv2
 
# load the image and show it
image = cv2.imread("screen.jpg")
	
#print image.shape

cropped = image[650:1550, 0:1920]
#cv2.imwrite( "test.jpg", cropped );
cv2.imshow("cropped", cropped)
#os.system('rm -rf screen')
cv2.waitKey(0)
