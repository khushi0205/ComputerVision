from asyncio import as_completed
import numpy as np
import cv2
from matplotlib import pyplot as plt
img2 = cv2.imread("car3.png")
img = cv2.imread("messi.png")
#color = [0,255,0]

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#hard = cv2.copyMakeBorder(img, 10,20, 10, 10, cv2.BORDER_CONSTANT, value=color)

#plt.subplot(223),plt.imshow(hard),plt.title('hard border')
#plt.show()

ball = img[240:290, 215:270]
img[245:340, 40: 95] = ball
img = cv2.resize(img, (450,340))
img2 = cv2.resize(img2, (450,340))

#dst = cv2.add(img, img2)
dst = cv2.addWeighted(img , 0.7, img2, 0.3, 0)
cv2.imshow('img', dst)
#cv2.setMouseCallback('img', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()