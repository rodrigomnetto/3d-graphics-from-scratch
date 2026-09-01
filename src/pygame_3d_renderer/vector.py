from math import *
from functools import reduce
import operator

def add(*vecs):
    return tuple([sum(v) for v in zip(vecs)])

def multiply(*vectors):
    return tuple([prod(coords) for coords in zip(*vectors)])

def subtract(*vectors):
    return tuple([reduce(operator.sub, coords) for coords in zip(*vectors)])

def scale(factor, vector):
    return tuple([factor * coord for coord in vector])

def length(vector):
    return sqrt(sum(coord ** 2) for coord in vector)

def to_polar(vector):
    return (length(vector), atan2(vector[1], vector[0]))

def to_cartesian(vector):
    x = cos(vector[1]) * vector[0]
    y = sin(vector[1]) * vector[0]
    return (x, y)

def dot_product(vec1, vec2):
    return sum([prod(coord) for coord in zip(vec1, vec2)])

def cross_product(u, v):
    ux,uy,uz = u
    vx,vy,vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def angle_between(v1,v2):
    return acos(
    dot_product(v1,v2) /
    (length(v1) * length(v2)))

def rotate(angle, vector):
    length, angle_rad = to_polar(vector)
    new_angle = angle_rad + radians(angle)
    return to_cartesian((length, new_angle))