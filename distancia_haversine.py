from math import *

def haversine(raio, lat1, long1, lat2, long2):
    calc_raio = 2 * raio
    calc_lat = ((lat2) - (lat1)) / 2
    calc_long = (long2 - long1) / 2
    parenteses = (sin(radians(calc_lat)) ** 2) + (cos(radians(lat1)) * cos(radians(lat2))) * (sin(radians(calc_long)) ** 2)
    d = calc_raio * asin(sqrt(parenteses))
    return d