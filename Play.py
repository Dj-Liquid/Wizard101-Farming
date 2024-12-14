import cv2
import numpy as np
import keyboard
import mouse
import time
import threading
import pygetwindow as gw


threshold = .8
yellow = (0, 255, 255)
green = (0, 255, 0)
pause_State = True
stop_threads = False
#WizardGraphicalClient
#Wizard101

def Choose_Spell(position):
    mouse.click(left)
    
    
def Enchant(epic_position,zand_position):
    Choose_Spell(epic_position)
    Choose_Spell(zand_position)

def Play_Round():
    positions = Get_Cards()
    print(positions)
    #Enchant(positions[0],positions[1])

def Get_Cards():
    menu = cv2.imread('Menu.png')
    enchant = cv2.imread('Epic.png')
    attack = cv2.imread('Zand_the_Bandit.png')
    cards = [[enchant,yellow],[attack,green]]
    card_height, card_width = cards[0][0].shape[:-1]
    locations = []
    
    for card in cards:
        match = cv2.matchTemplate(menu, card[0], cv2.TM_CCOEFF_NORMED)
        location = np.where(match >= threshold)
        for point in zip(*location[::-1]):  # Switch columns and rows
            cv2.rectangle(menu, point, (point[0] + card_width, point[1] + card_height), card[1], 2)
            locations.append([point, (point[0] + card_width, point[1] + card_height)])
    
    cv2.imwrite('result.png', menu)
    cv2.imshow('Result',menu)
    cv2.waitKey(0)
    
    return locations
'''
def Test():
    global pause_State
    while True:
        time.sleep(.1)
        if not pause_State:
            print(mouse.get_position())
        if keyboard.is_pressed('z'):
            pause_State*=-1
'''
'''
def Record():
    global stop_threads
    
    # search for the window, getting the first matched window with the title
    w = gw.getWindowsWithTitle("Wizard101")[0]
    # activate the window
    w.activate()


    # Define video codec and frames per second
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30
    record_seconds = 10

    # Create the video writer object
    out = cv2.VideoWriter("video_out.mp4v", fourcc, fps, tuple(w.size))
    while not stop_threads:
        # Capture a screenshot
        img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))

        # Convert to a numpy array
        frame = np.array(img)

        # Convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Draw the rectangle on the image
        Get_grid(frame)
        
        # Write the frame to the video file
        out.write(frame)
    cv2.destroyAllWindows()
    out.release()
    print(f"Recording thread is stopping")

'''

#recording_thread = threading.Thread(target=Record, args=())
playing_thread = threading.Thread(target=Get_Cards, args=())
#recording_thread.start()
playing_thread.start()



try:
    while True:
        time.sleep(.1)
except KeyboardInterrupt:
    stop_threads = True
    #recording_thread.join()
    playing_thread.join()
    print("Program terminated")
