# #Trying to control a plane and stuff / Mission Planner
import sys
sys.path.append(r"C:\Python27\Lib")
sys.path.append(r"C:\Python27\Lib\site-packages")
# import serial, os, threading
import math
from math import radians, cos, sin, sqrt, atan2
import clr
import time
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") #Includes utilities class
# from MissionPlanner.Utilities import Locationwp
# #Last 4 lines of code are straight copied
#
def distance(lat1, lon1, lat2, lon2):
    #Returns distance travelled in meters, coordinates are in degrees
    r_e = 6378000 #Radius of Earth in meters


    lat1 = math.radians(float(lat1))
    lat2 = math.radians(float(lat2))
    lon1 = math.radians(float(lon1))
    lon2 = math.radians(float(lon2))
    dLat = lat2 - lat1
    dLon = lon2 - lon1
    #
    a = math.sin(0.5 * dLat)**2 + math.sin(0.5 * dLon)**2 math.cos(lat1) * math.cos(lat2) #It doesn't like this line!
    # c = 2 * math.atan2(sqrt(a), math.sqrt(1 - a))
    c = .003
    return r_e * c

print 'Start Script'
for chan in range(1,9):
    Script.SendRC(chan,1500,False)
    Script.SendRC(3,Script.GetParam('RC3_MIN'),True)

Script.Sleep(5000)

while cs.lat == 0:
    print 'Waiting for GPS'
    Script.Sleep(1000)

print 'Got GPS'
jo = 10 * 13
print jo
Script.SendRC(3,1000,False)
Script.SendRC(4,2000,True)
cs.messages.Clear()
Script.WaitFor('ARMING MOTORS',30000)
Script.SendRC(4,1500,True)
print 'Motors Armed!'
Script.SendRC(3,1700,True)
#
# print 'Running Script'
#
# Script.ChangeMode("Guided") #Changed flight to guided
# item = MissionPlanner.Utilities.Locationwp() #creating waypoint
#
# dist_tolerance = 15 #(m)
# ber_tolerance = 45 #heading tolerance
# #Both are something used in an example code
#
# alt = 100.0000 #altitude in meters
# Location.lat.SetValue(item, 25) #sets latitude
# Location.lng.SetValue(item, 135) #sets longitude
# Location.alt.SetValue(item, alt) #sets altitude
# print "Target Set"
#
# MAV.setGuidedModeWP(item) #Tells UAV "go to" the set lat/long @ alt
# print "Target in Sight"
#
# Good = True
# goal_dist = distance(0, 0, math.radians(25), math.radians(135))
#
# while Good == True:
#     speed_g = cs.groundspeed
#     alt = cs.alt
#     wp_dist = distance(cs.lat, cs.lng, math.radians(25), math.radians(135))
#     print wp_dist
#     ber_error = cs.ber_error
#
#     if(math.fabs(goal_dist - wp_dist) <= dist_tolerance):
#         if (math.fabs(ber_error) <= ber_tolerance):
#             print "Fire in the hole"
#             break
#         else:
#             print "Heading outside of threshold, go around!"
#             Good = False
#
#     else:
#         print 'Outside of threshold.'
#         time.sleep(1.0)
#
#     print 'Issue with making it to target'
