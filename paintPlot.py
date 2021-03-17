import pyautogui
import subprocess
from scipy.integrate import odeint
import numpy as np
import time

def openPaint():
    subprocess.Popen('C:\Windows\System32\mspaint.exe')

def draw_line(x1, y1, x2, y2):
    pyautogui.moveTo(x1,y1)
    pyautogui.dragTo(x2,y2, button = "left")

def makeAxis(x1, y1, x2, y2, arrowLength = 15, axisOffset = 40):
	xInit = x1
	yInit = y2
	axisLengthX = x2 - x1
	axisLengthY = y2 - y1

	axisArrowLength = np.sqrt(2)*arrowLength	# Length along an axis

	# Drawing x-axis
	draw_line(xInit - axisOffset, yInit, xInit + axisLengthX, yInit)
	draw_line(xInit + axisLengthX, yInit, xInit + axisLengthX - axisArrowLength, yInit - axisArrowLength)
	draw_line(xInit + axisLengthX, yInit, xInit + axisLengthX - axisArrowLength, yInit + axisArrowLength)

	# Drawing y-axis
	draw_line(xInit, yInit + axisOffset, xInit, yInit - axisLengthY)
	draw_line(xInit, yInit - axisLengthY, xInit + axisArrowLength, yInit - axisLengthY + axisArrowLength)
	draw_line(xInit, yInit - axisLengthY, xInit - axisArrowLength, yInit - axisLengthY + axisArrowLength)


def plot(x1, y1, x2, y2, X, Y):
    #(x1,y1)------------------------
    #|                             |
    #|                             |
    #|                             |
    #|                             |
    #--------------------------(x2, y2)

    yMin = np.min(Y)
    yMax = np.max(Y)
    xMin = np.min(X)
    xMax = np.max(X)

    # Distance between the fist and last X coordinate
    xPointDist = xMax - xMin
    yPointDist = yMax - yMin
    
    # Distance between buttom left and buttom right corner
    xPlotDist = x2 - x1
    yPlotDist = y2 - y1

    # Determine distance of one point in pixels
    xPixelsPerPoint = xPlotDist / xPointDist
    yPixelsPerPoint = yPlotDist / yPointDist

    # Plot inside rectangle defined by (x1,y1) and (x2,y1)
    xOld = x1 + (X[0] - xMin) * xPixelsPerPoint
    yOld = y1 + (yMax - Y[0]) * yPixelsPerPoint
    for x, y in zip(X[1:], Y[1:]):
        xLineEnd = x1 + (x - xMin) * xPixelsPerPoint
        yLineEnd = y1 + (yMax - y) * yPixelsPerPoint
        draw_line(xOld, yOld, xLineEnd, yLineEnd)
        xOld = xLineEnd
        yOld = yLineEnd

def vanDerPol(x, t):
    x1 = x[0]
    x2 = x[1]
    mu = 2
    dxdt = np.array([x2, mu*(1 - x1**2)*x2 - x1])
    return dxdt
    

# Defining plot box
#(x1,y1)----------------------------
    #|                             |
    #|                             |
    #|                             |
    #|                             |
    #--------------------------(x2, y2)
x1, y1 = 200, 240
x2, y2 = 870, 640

# Number of points
N = 300

# Altering delay between each move
pyautogui.PAUSE = 1/4000

# Open Paint and wait
openPaint()
time.sleep(1)

# Creating axis
makeAxis(x1, y1, x2, y2, 15)
'''
# Plotting Van der Pol problem
t = np.linspace(0, 10, 300)
x0 = [0, 1]
x = odeint(vanDerPol, x0, t)
'''
x = np.linspace(0, 10, 300)
y = x
plot(x1, y1, x2, y2, x, x)
