import pyautogui
import time
from pynput import keyboard

# User inputs
isInfinity = input("Do you want to click infinitely? (yes/no): ").lower()
if isInfinity != "yes":
    try:
        howOften = int(input("How many times do you want to click?: "))
        if howOften <= 0:
            raise ValueError
    except ValueError:
        print("You must enter a positive number.")
        exit()

try:
    interval = float(input("Click interval (in seconds): "))
except ValueError:
    print("Invalid interval.")
    exit()

exitKey = input("Key to STOP clicking (pause): ").lower()
restartKey = input("Key to START clicking (resume): ").lower()

clicking = True  # Start in clicking mode
current_click = 0  # Counter for non-infinite mode

# Key listener
def on_press(key):
    global clicking
    try:
        if key.char == exitKey:
            clicking = False
            print("[Paused]")
        elif key.char == restartKey:
            clicking = True
            print("[Resumed]")
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Starting in 5 seconds... Press your stop key to pause, restart key to resume.")
time.sleep(5)

# Main loop
if isInfinity == "yes":
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(interval)
else:
    while current_click < howOften:
        if clicking:
            pyautogui.click()
            current_click += 1
            time.sleep(interval)

print("Done clicking.")
