# IMPORT PI FROM MATH
from math import pi


# Converts degrees to rad
def deg_to_rad(degrees):

    # Converts and returns radians
    radians_ = degrees * (pi / 180)
    return radians_


# Converts radians to degrees
def rad_to_deg(radians):

    # Converts and then returns
    degrees_ = radians * (180 / pi)
    return degrees_
