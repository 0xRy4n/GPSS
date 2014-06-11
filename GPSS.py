# Module Name:  GPSS - GPSS is a Precise Scribbling System
# Author:       Ryan J Gordon
#                   Contact Email:  RyanJeffreyGordon@gmail.com
#                   Website:        www.RJGordon.net

#                ~ Scribbling with Precision ~
#   GPSS allows for precise movement of a Scribbler 2 Robot by allowing a user to
#   input real distances and angle degrees for movement and turns while compensating 
#   for loss of RPM do to variations in battery voltage. All measurements are done
#   in the metric unit centimeters.

import math
from myro import *

# CONSTANTS #
FORWARD, F = 1, 1
BACK, B = -1, -1
RIGHT, R = 10, 10
LEFT, L = -10, -10

"""*************************************************************************************"""
""" Calculation Functions - These should not be called by individuals using the module. """

########################################################################################
# Function:     getDPS()
# Description:  calculates current distance per second in correlation to the battery voltage.
# Parameters :  none
# Returns:      dps ; type float -- distance per second robot can travel in centimeters
def calcDPS():
    wheelRadius = 3.96508
    batVolt = getBattery()
    rpm = 20.02256 * batVolt - 100.29672
    if rpm < 20:
        rpm = 20
    rps = rpm / 60
    dpr = math.pi * (2 * wheelRadius)
    dpm = dpr * rpm
    dps = dpm / 60
    return(dps)
    
########################################################################################
# Function:     calcTurnDur(degrees)
# Description:  calculates time needed to turn a specified amount of degrees.
# Parameters:   distance : type float -- desired turn amount in degrees.
# Returns:      duration : type float -- time required to make desired turn in seconds
def calcTurnDur(degrees):
    scribRadius = 7.9375
    turnDeg = degrees
    dps = calcDPS()
    arcLen = (turnDeg / 360) * ((2 * math.pi) * scribRadius)
    duration = arcLen / dps 
    return(duration)
    
#########################################################################################
# Function:     calcMoveDur(distance)
# Description:  calculates time needed to move a specified distance in centimeters.
# Parameters:   distance : type float -- desired distance in centimeters.
# Returns:      duration : type float -- time required to move desired distance in seconds.
def calcMoveDur(distance):
    moveDis = distance
    dps = calcDPS()
    duration = moveDis / dps
    return(duration)
    
    
    
"""************************************************************************************"""    
""" Movement Procedures - These are meant to be called by individuals using the module """

#########################################################################################
# Procedure:     move(direction, distance)
# Description:   moves desired distance in centimeters in the specified direction.
# Parameters:    direction -- BACK or B for backwards, FORWARD or F for forwards.
#                distance ; type float -- distance in centimeters.                               
def move(direction, distance):
    try:
        moveDis = float(distance)
    except:
        print("Not a valid numerical distance.")
    moveDur = calcMoveDur(moveDis)
    if direction == FORWARD:
        forward(1, moveDur)
    elif direction == BACK:
        backward(1, moveDur) 
    else:
        print("Invalid direction. Please use FORWARD / F, or BACK / B.")


##########################################################################################
# Procedure:      turn(direction, degrees)
# Description:    turns in desired direction by specified degrees.
# Parameters:     direction -- RIGHT or R for right, LEFT or L for left.
#                 degrees ; type float -- desired turn amount in degrees.
def turn(direction, degrees):
    try:
        turnDeg = float(degrees)
    except:
        print("Not a valid numerical degree.")
    turnDur = calcTurnDur(turnDeg)
    if direction == RIGHT:
        turnRight(1, turnDur)
    elif direction == LEFT:
        turnLeft(1, turnDur)
    else:
        print("Invalid direction. Please use RIGHT / R, or LEFT / L.")

    
    
    
