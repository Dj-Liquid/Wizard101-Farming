import tkinter as tk
import Play
import keyboard

def Start():
    label.config(text="Started")
    print("Start")
    Play.Play()
    
def Stop():
    label.config(text="Stopped")
    print("Stop")
    Play.Stop()
  
def Pause_State():
    paused = not paused
    if paused:
        label.config(text="Playing")
        print("Unpaused")
        keyboard.send('®')
    else:
        label.config(text="Paused")
        print("Paused")
        keyboard.wait('®')
    
paused = True       
# Set up the main window
root = tk.Tk()
root.title("Wizard101 Farm GUI")

# Add a label
label = tk.Label(root, text="Press the button to Start/Stop the program")
label.pack()


# Add a button
button = tk.Button(root, text="Start", command=Start)
button.pack()

button = tk.Button(root, text="Stop", command=Stop)
button.pack()

button = tk.Button(root, text="Pause", command=Pause_State)
button.pack()

# Run the application
root.mainloop()