import cv2
import pytesseract

# process the image given by the user
def image_preprocess():
    confg = r'--oem 3 --psm 6'

    img = cv2.imread('image.png')
    boxes = pytesseract.image_to_data(img, config = confg)
    # print(boxes)
    line = []
    for x, b in enumerate(boxes.splitlines()):
        # print(x)
        if x > 4:
            b = b.split()   
            # print(b)
            if int(b[0]) == 4 and int(b[10]) == -1:
                break
            elif len(b) ==  12:
                line.append(b)
    img2 = img.copy()
    max_height = []      
    max_width = 0
    for ln in line:
        print(ln)
        x, y, w, h = int(ln[6]),int(ln[7]),int(ln[8]),int(ln[9]) 
        max_height.append(y+h)
        max_width += w
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 1)
    print(max(max_height))
    print(max_width)
    img2 = img2[0:max(max_height), 0:max_width+100]
    cv2.imshow('cropped image', img2)
    cv2.imwrite('Trimmed_Image.png', img2)
    # cv2.imshow('image', img)
    
    
    cv2.waitKey(0)

image_preprocess()