#-----------------------------------------------------------------------------#
                    #INSTRUCTIONS
#1)Run Script in simulation
#2)Arm Device using the GUI
#3)Do the "Start Mission" action with the GUI
#4) ????
#5) Profit.

#It worked for me, if it doesn't for you then idk
#-----------------------------------------------------------------------------#

#first starter script
#import stuff
import sys
import math
import clr
import time
import System
from System import Byte

#this bit needs to go at the start of every script for things to work smoothly
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink") # includes the Utilities class
import MAVLink

idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)

#set a series of points
#points need to be centered about the planes current position
homelat = cs.lat
homelong = cs.lng
#give each intended waypoint a position, in latitude, longitude, and altitude
#don't forget to set the home wp for the first one!
#takeoff = Locationwp()
#Locationwp.id.SetValue(takeoff, int(MAVLink.MAV_CMD.TAKEOFF))
#Locationwp.p1.SetValue(takeoff, pitch)
#Locationwp.alt.SetValue(takeoff, launch_altitude)
home = Locationwp().Set(cs.lat,cs.lng, 100, id)
#command to be carried out once reaching the waypoint
Locationwp.id.SetValue(home, int(MAVLink.MAV_CMD.TAKEOFF))
#desired pitch at the waypoint (I think)
Locationwp.p1.SetValue(home, 10)
#altitude at which the action will be carried out at
Locationwp.alt.SetValue(home,0)
wp1 = Locationwp().Set((homelat+.0001),(homelong+.0001),100, id)
wp2 = Locationwp().Set((homelat+.0002),(homelong-.0001),100, id)
wp3 = Locationwp().Set((homelat-.0001),(homelong-.0001),100, id)
#set the total number of waypoints
MAV.setWPTotal(4) #don't forget to count the home waypoint

#upload each waypoint to mission planner
#the syntax for uploading waypoints is as follows:
# MAV.setWP(-Coordinates-,-upload order-,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
#still kind of iffy on what the 3rd argument is
#upload order is indexed at zero
print("upload home")
MAV.setWP(home,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
#print("upload takeoff")
#MAV.setWP(takeoff,1,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
print("upload wp1")
MAV.setWP(wp1,2,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
print("upload wp2")
MAV.setWP(wp2,3,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
print("upload wp3")
MAV.setWP(wp3,4,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT)
print("final ack")
MAV.setWPACK()
            
print("Waypoints set")

	
print 'TAKEOFF MISSION'

