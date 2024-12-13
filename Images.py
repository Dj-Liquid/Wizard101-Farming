import cv2
import numpy as np

threshold = .8
yellow = (0, 255, 255)
green = (0, 255, 0)

menu = cv2.imread('Menu.png')
enchant = cv2.imread('Epic.png')
attack = cv2.imread('Zand_the_Bandit.png')
cards = [[enchant,yellow],[attack,green]]
card_height, card_width = cards[0][0].shape[:-1]


for card in cards:
    match = cv2.matchTemplate(menu, card[0], cv2.TM_CCOEFF_NORMED)
    location = np.where(match >= threshold)
    for point in zip(*location[::-1]):  # Switch columns and rows
        cv2.rectangle(menu, point, (point[0] + card_width, point[1] + card_height), card[1], 2)


cv2.imwrite('result.png', menu)