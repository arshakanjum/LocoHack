import cv2
import operator

def captch_ex(file_name):
    img = cv2.imread(file_name)

    img = img[650:1750, 0:1920]
    
 


    img_final = cv2.imread(file_name)


    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY) 

    largest_area=0;
    largest_contour_index=0
    i=0
    a={}
    aa=0
    bb=0
    cc=0
    dd=0
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) 
    dilated = cv2.dilate(new_img, kernel, iterations=15)  

    #imS = cv2.resize(dilated, (960, 540)) 
    #cv2.imshow('captcha_result', imS)
   #cv2.waitKey()

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        
        area = cv2.contourArea(cnt)
        a[i]=area
        i=i+1
    #print a
    sorted_a = sorted(a.items(), key=operator.itemgetter(1))
    
    b=map(list, zip(*sorted_a))
 

    
    aa=b[0][len(b[0])-1]
    bb=b[0][len(b[0])-2]
    cc=b[0][len(b[0])-3]
    dd=b[0][len(b[0])-4]

    i=i-1

    i=1
    for n in [aa,bb,cc,dd]:
        [x, y, w, h] = cv2.boundingRect(contours[n])
        #print [x,y,w,h]
        #print n
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        crop=img[y:y+h,x:x+w]
        if n==aa:
            cv2.imwrite( "test.jpg", crop )
        else:
            cv2.imwrite( "ans"+str(i)+".jpg", crop )
            i=i+1    
        #imS = cv2.resize(crop, (960, 540)) 
        #cv2.imshow('captcha_result', crop)
        #cv2.waitKey()

file_name = 'screen.jpg'
captch_ex(file_name)


