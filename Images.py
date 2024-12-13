import cv2
import numpy as np

img_rgb = cv2.imread('Menu.png')
enchant = cv2.imread('Epic.png')
w1, h1 = enchant.shape[:-1]
res1 = cv2.matchTemplate(img_rgb, enchant, cv2.TM_CCOEFF_NORMED)

attack = cv2.imread('Zand_the_Bandit.png')
w2, h2 = attack.shape[:-1]
res2 = cv2.matchTemplate(img_rgb, attack, cv2.TM_CCOEFF_NORMED)

threshold = .8
loc1 = np.where(res1 >= threshold)
loc2 = np.where(res2 >= threshold)
for pt in zip(*loc1[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + h1, pt[1] + w1), (0, 255, 255), 2)

for pt in zip(*loc2[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + h2, pt[1] + w2), (0, 255, 0), 2)

cv2.imwrite('result.png', img_rgb)