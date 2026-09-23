"""
The area of a circle can be calculated
using its radius and the mathematical constant π.
Area of a circle formula:   "Area = π × r²"
"""

#Using hardcoded pi value
# PI = float(input("Enter the PI value:"))
PI = 3.14159
radius = float(input("Enter the radius of the circle:"))

area = PI * radius ** 2
print(f"Area of the circle is: {area}")

#----------------------------------------------------------------------------

#Using math.pi
from math import pi


radius = float(input("Please enter the radius of the circle: "))
area = pi * radius ** 2
print(f"The area of the circle is:  {round(area, 3)}")

#----------------------------------------------------------------------------


#Using math.pow()
from math import pi, pow


r = float(input("Please enter the radius of the circle: "))
area = pi * pow(r, 2)
print(f"The area of the circle is: {round(area, 2)}")

#----------------------------------------------------------------------------


#Using numpy.pi
"""
If you don't have numpy on your machine, install it with pip:
    $ pip install numpy
"""
from numpy import pi


r = float(input("Please enter the radius of the circle: "))
area = round(pi * r**2, 2)
print(f"Area of the circle is: {area}")
