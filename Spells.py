import keyboard
import mouse
import time



def Choose_Spell(position):
    mouse.click(left)
    
    
def Enchant(epic_position,zand_position):
    Choose_Spell(epic_position)
    Choose_Spell(zand_position)

try: 
    while True:
        time.sleep(.1)
        print(mouse.get_position())
        if keyboard.is_pressed('z'):
            keyboard.wait('x')
except KeyboardInterrupt:
    print("Program terminated")