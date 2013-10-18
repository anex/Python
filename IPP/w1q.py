#1
#2

"""
p = True
q = True

if not (p or not q):
    print True
else:
    print False
"""

#3
"""
n = 123.4

print ((n - n % 10) / 10) % 10
print ((n - n % 10) % 100) / 10
"""

#4

#5
"""
def func(x):
    #result = (-5 * (x ** 5)) + (69  * (x ** 2)) -47
    result = (-5 * (x ** 5)) + (69 * (x ** 2)) - 47
    return result

print func(0) 
print func(1) 
print func(2) 
print func(3) 
"""

#6
"""
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    fv = present_value * ((1 + rate_per_period) ** periods)

    return fv
    

print "$1000 at 2% compounded daily for 3 years yields $",  future_value(1000,  .02,  365,  3)
#print future_value(500, .04, 10, 10)
"""

#7
"""
import math
def area_polygon(n,s):
    area = (0.25 * n * (s ** 2)) / ( math.tan(math.pi/n) ) 
    return area

print area_polygon(7,3)
"""

#8

#9
"""
import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale,  point_y * scale

project_to_distance(2, 7, 4)
"""
