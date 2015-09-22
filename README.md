NOTICE: The Calico version of Myro has been updated and GPSS is no longer relevant.

GPSS is a Precise Scribbling System
======
Scribbling with Precision
-------------------------

GPSS is a simple python module that works in unity with IRPE's Myro. It stands for GPSS is a Precise Scribbling System. The goal of GPSS is to allow for precise and consistant operation of the Scribbler 2 robot's motors. In typical use, one operating a Scribbler robot using the standard Myro module cannot specify precise movement procedures such as turning to a specific degree, or moving a specific distance. Instead, users must specify a duration to move the robot and hope that it is the proper duration for the exact measurement of movement they desire. However, even if one does manage to find the correct timing for the movement they desire, that timing will not be consistant. The RPM of the Scribbler's wheel motors slows perpetually as the voltage of the battery lowers from full. Basically, the timing that will allow you the turn 90 degrees one moment, will only turn it 70 degrees 5 minutes later. 

Using the given functions in Myro, it is impossible to get completely consistant results from the execution of the same code over a span of any and all duration. GPSS fixes that.

Using GPSS, a user can specify the exact degree they want the Scribbler turn to, or the exact distance they want the Scribbler to move to, and the Scribbler will consitantly reproduce the same results regardless of battery voltage.

Documentation
=============
There are only two precedures that should be called by individuals using GPSS. All measurements are done in centimeters.

Setup
-----
To use GPSS, simply place the *GPSS.py* file either in your Python disribution's module library directory, or, in the same directory as the file you want to use it with. After this is done, you may simply import GPSS normally. Please make sure to import Myro **before** importing GPSS. 

Your imports should look something like this:

        from myro import *
        from GPSS import *

Moving Straight
----------------
        move(direction, distance)
**direction** - *can be either FORWARD or F to move forwards, and BACK or B to move backwards.*

**distance** - *the desired distance to move in centimeters.*

Turning
-------
        turn(direction, degrees)
**direction** - *can be either RIGHT or R to turn right, and LEFT or L to turn left.*

**degrees** - *desired degree to turn to.*
