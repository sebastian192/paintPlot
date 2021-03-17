import pyautogui
import sys

# Remove stupid failsafe
pyautogui.failsafe = False
pyautogui.PAUSE = 0

# Save current position 
xMouse, yMouse = pyautogui.position()

# Making window active and scrolling
pyautogui.click(x = 630, y = 550)
pyautogui.scroll(int(sys.argv[1]))

# Move back
pyautogui.moveTo(xMouse, yMouse)