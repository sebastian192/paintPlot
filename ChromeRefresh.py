import pyautogui
import time

# Remove stupid failsafe
pyautogui.failsafe = False
pyautogui.PAUSE = 0

# Save current position 
xMouse, yMouse = pyautogui.position()

# Press on google chrome refresh icon
xClick = 86
yClick = 59
pyautogui.click(xClick, yClick)

# Move back
pyautogui.moveTo(xMouse, yMouse)
