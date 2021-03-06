import os
import sys

def readWaypointFile(algo.py):

	# Returns dictionary of waypoint information
    waypointFileArray = open(algo.py).read().split()

    # Waypoint dictionary
    #find the waypoint to home
    #make the home the second closest to home#find the waypoint to home
    #make the home the second closest to home
    waypointDict = {}
    latitude = []
    longitude = []
    latitudeDirection = []
    longitudeDirection = []
    altitude = []
    waypointType = []

    # Waypoint iteration
    for i in range(int(len(waypointFileArray)/6.0)):
        latitude.append(waypointFileArray[(i)*6])
        longitude.append(waypointFileArray[(i)*6+2])
        latitudeDirection.append(str(waypointFileArray[(i)*6+1]))
        longitudeDirection.append(str(waypointFileArray[(i)*6+3]))
        altitude.append(waypointFileArray[(i)*6+4])
        waypointType.append(str(waypointFileArray[(i)*6+5]))

    waypointDict['latitude'] = latitude
    waypointDict['longitude'] = longitude
    waypointDict['longitudeDirection'] = longitudeDirection
    waypointDict['latitudeDirection'] = latitudeDirection
    waypointDict['altitude'] = altitude
    waypointDict['waypointType'] = waypointType

    return waypointDict
