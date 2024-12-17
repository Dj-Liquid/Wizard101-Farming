import cv2
import numpy as np
import keyboard
import mouse
import time
import threading
import pygetwindow as gw
import pyautogui

fights = 0
threshold = .8
yellow = (0, 255, 255)
green = (0, 255, 0)
white = (255, 255, 255)
pause_State = False
stop_threads = False
w = gw.getWindowsWithTitle("Wizard101")[0]
enchant = cv2.imread('Epic.png')
attack = cv2.imread('Zand_the_Bandit.png')
enchanted_attack = cv2.imread('Epic_Zand.png')
cards = [[enchant,yellow],[attack,green],[enchanted_attack,white]] 
card_height, card_width = cards[0][0].shape[:-1]

def Choose_Spell(position):
    mouse.move(position[0], position[1], absolute=True, duration=0.15)
    time.sleep(.5)
    mouse.click('left')

def Attack():
    global fights
    while True:
        location = Match(cards[-1])
        if location != '':
            break
        time.sleep(3)
    Choose_Spell(location)
    fights+=1
        
    
def Enchant(epic_position,zand_position):
    Choose_Spell(epic_position)
    Choose_Spell(zand_position)

def Play_Round():
    while True:
        positions = Get_Cards()
        if len(positions)>1:
            break
        else:
            keyboard.press('w')
            time.sleep(.1)
            keyboard.release('w')
            time.sleep(5)
        print("Checking")
        
    Enchant(positions[0],positions[1])
    mouse.move(0, 400, absolute=False, duration=0.15)
    time.sleep(2.5)
    Attack()
    mouse.move(0, 400, absolute=False, duration=0.15)
    for x in range(30):
        time.sleep(1)
        print(x)

def Match(card):
    location = ''
    w.activate()
    img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
    #menu = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    menu = cv2.imread('Menu.png')
    match = cv2.matchTemplate(menu, card[0], cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= threshold)
    for point in zip(*loc[::-1]):
        cv2.rectangle(menu, point, (point[0] + card_width, point[1] + card_height), card[1], 2)
        location = [point[0] + card_width // 2, point[1] + card_height // 2]
        
    cv2.imwrite('Most_recent_Image.png', menu)
    return location
    
    

def Get_Cards():
    locations = []
    locations_upd = []
    for card in cards[:-1]:
        locations.append(Match(card))
        if locations[0] == '':
            return []
    for location in locations:
        if len(locations_upd)==0:
            locations_upd.append(location)
        else:
            if abs(locations_upd[0][0] - location[0]) >= 10:
                locations_upd.append(location)
    print("Success",locations_upd)  
    return locations_upd
    
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


def Start():
    #recording_thread = threading.Thread(target=Record, args=())
    #playing_thread = threading.Thread(target=Play, args=())
    #recording_thread.start()
    #playing_thread.start()
    Play()
    
    
def Stop():
    raise KeyboardInterrupt
    
def Pause_State():
    pass
  
def Play():
    try:
        while True:
            Play_Round()
    except KeyboardInterrupt:
        #recording_thread.join()
        #playing_thread.join()
        print("#of fights completed: ",fights)
        print("Program terminated")

