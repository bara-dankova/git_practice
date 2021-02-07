from math import pi, tan, cos

g = 9.81
v0 = 44
theta = 80 * (pi/180)
x = 0.5
h0 = 1


height = h0 + x * tan(theta) - ((g*(x**2))/(2*((v0 * (cos(theta)**2))

print(height)

input()