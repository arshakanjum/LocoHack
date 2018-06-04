import cv2
 
# load the image and show it
image = cv2.imread("screen.jpg")
	
#print image.shape

cropped = image[950:1100, 200:900]
cv2.imwrite( "ans1.jpg", cropped );
#cv2.imshow("cropped", cropped)
#os.system('rm -rf screen.jpg')
cv2.waitKey(0)
