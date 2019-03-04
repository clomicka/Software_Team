#Trying to control a plane and stuff / Mission Planner
import sys
sys.path.append(r"c:\python27\lib")
import math
import clr
import time
clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") #Includes utilities class
from MissionPlanner.Utilities import Locationwp
#Last 4 lines of code are straight copied

def distance(lat1, lon1, lat2, lon2):
    #Returns distance travelled in meters, coordinates are in degrees
    r_e = 6378000 #Radius of Earth in meters

    from math import radians, cos, sin, sqrt, atan2
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    dLat = lat2 - lat1
    dLon = lon2 - lon1

    a = sin(0.5*dLat)**2 + sin(0.5*dLon)**2 cos(lat1) * cos(lat2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r_e * c


print 'Running Script'

Script.ChangeMode("Guided") #Changed flight to guided
item = MissionPlanner.Utilities.Locationwp() #creating waypoint

dist_tolerance = 15 #(m)
ber_tolerance = 45 #heading tolerance
#Both are something used in an example code

alt = 100.0000 #altitude in meters
Location.lat.SetValue(item, 25) #sets latitude
Location.lng.SetValue(item, 135) #sets longitude
Location.alt.SetValue(item, alt) #sets altitude
print "Target Set"

MAV.setGuidedModeWP(item) #Tells UAV "go to" the set lat/long @ alt
print "Target in Sight"

Good = True
goal_dist = distance(0, 0, math.radians(25), math.radians(135))

while Good == True:
    speed_g = cs.groundspeed
    alt = cs.alt
    wp_dist = distance(cs.lat, cs.lng, math.radians(25), math.radians(135))
    print wp_dist
    ber_error = cs.ber_error

    if(math.fabs(goal_dist - wp_dist) <= dist_tolerance):
        if (math.fabs(ber_error) <= ber_tolerance):
            print "Fire in the hole"
            break
        else:
            print "Heading outside of threshold, go around!"
            Good = False

    else:
        print 'Outside of threshold.'
        time.sleep(1.0)

    print 'Issue with making it to target'
