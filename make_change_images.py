# -*- coding: utf-8 -*-
"""
Created on Mon May 12 18:33:43 2025

@author: Kamila
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


#make an airport dictionary ex {0:BLI,...}
airport_dict = {}
airport_string = 'BLIPDXEUGMFROAKSCKFATMRYSMXLAXSNAPSPSANRNOLASPHXIWAGEGPSCGPIGTFMSOBZNBIL\
BOIIDAPVUGJTDENELPEYWSATAUSLRDMFEHOUMOTGFKBISFARRAPFSDOMAGRIICTTULOKCSTCMSPDSMCIDMLIMCI\
SGFXNALITSHVMSYATWRFDMDWPIABMISPIBLVTVCGRRFNTSBNTOLFWAINDEVVSDFVPSBNAMEMPIEBGRPBGPSM\
BOSPVDROCSYRALBIAGELMSWFABEEWRCAKMDTPITDAYLCKHGRBWICVGCKBIADHTSROARICORFLEXTRIGSOSRQ\
TYSAVLUSACHAGSPMYRCHSSAVJAXSFBMLBPBIFLLPGD'
for i in range(123):
    airport_dict.update({i:airport_string[:3]})
    airport_string = airport_string[3:]


# make png images for all the airport codes
for i in range(123):
    airport_code=airport_dict[i]

    # Create a white image
    img = np.zeros((100,100,3), np.uint8)
    #img.fill(255)
    # Write some Text in red color
    font                   = cv2.FONT_HERSHEY_PLAIN
    bottomLeftCornerOfText = (5,60)
    fontScale              = 2.8
    fontColor              = (139,0,0)
    thickness              = 5
    lineType               = 2
    
    cv2.putText(img,airport_code, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        thickness,
        lineType)
    #convert to brg image
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/"+str(i)+".png", img_bgr)
    
    #make white spaces transparent
    from PIL import Image
    img = Image.open("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/"+str(i)+".png") 
    rgba = img.convert("RGBA") 
    datas = rgba.getdata() 
  
    newData = [] 
    for item in datas: 
        if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value 
            # storing a transparent value when we find a black colour 
            newData.append((255, 255, 255, 0)) 
        else: 
            newData.append(item)  # other colours remain unchanged 
      
    rgba.putdata(newData) 
    rgba.save("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/"+str(i)+".png", "PNG")


# make a blank png image
blank = np.zeros((100,100,3), np.uint8)
blank.fill(255)
cv2.imwrite("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/blank.png", blank)


# make a "calculate" png image
calc_img = np.zeros((400,900,3), np.uint8)
calc_img.fill(255)
# Write some Text
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (100,200)
fontScale              = 4
fontColor              = (0,0,0)
thickness              = 7
lineType               = 2

cv2.putText(calc_img,'CALCULATE', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)
cv2.cvtColor(calc_img, cv2.COLOR_RGB2BGR)
cv2.imwrite("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/calc_img.png", calc_img)


# make a "PLAY AGAIN" png image
again_img = np.zeros((400,900,3), np.uint8)
again_img.fill(255)
# Write some Text
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (100,200)
fontScale              = 4
fontColor              = (0,0,0)
thickness              = 7
lineType               = 2

cv2.putText(again_img,'PLAY AGAIN', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,
    lineType)
cv2.cvtColor(again_img, cv2.COLOR_RGB2BGR)
cv2.imwrite("C:/Users/Kamila/OneDrive/Desktop/Project0/map_game/again_img.png", again_img)
