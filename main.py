import cv2

img = cv2.imread('/Users/amritkumaryadav/Desktop/Chota Amrit.jpeg')

height,weidth = img.shape[:2]

max_height = 500
max_weidth = 250

cv2.imshow("Shrinked image", img)
key = cv2.waitKey()

if max_height < height or max_weidth < weidth :
    scaling_factor = max_height/float(height)
    if max_weidth/weidth < scaling_factor:
        scaling_factor = max_weidth/weidth
        
img = cv2.resize(img,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)

# cv2.imshow("Shrinking Image",img) # this is for to show the picture.
cv2.imwrite("Chotta_amrit_2.jpeg",img) # This will help to create the image same at the location of orginal image .

key = cv2.waitKey() # This is the key help to run the code until you close the image.