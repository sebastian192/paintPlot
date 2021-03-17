import pyautogui 
import sys

pyautogui.PAUSE = 0

pyautogui.moveTo(int(sys.argv[1]), int(sys.argv[2]))