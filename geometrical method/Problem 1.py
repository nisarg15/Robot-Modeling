import math
import matplotlib.pyplot as plt

x = 2
y = 3
alpha = 20
phi = 30
r = 0.25
ds = 35
x_points = []
y_points = []
L = 4
time = 400
n_intervals = 100
delta_t = (time/n_intervals)

for i in range(n_intervals):
    x_new = x + (r*ds*math.sin(math.radians(phi)))*delta_t
    y_new = y + (r*ds*math.cos(math.radians(phi)))*delta_t
    phi_new = phi + ((r*ds*math.sin(math.radians(alpha)))/L)*delta_t
    
    x_points.append(x_new)
    y_points.append(y_new)
    
    x = x_new
    y = y_new
    phi = phi_new
    
plt.scatter(x_points, y_points,color="black")
plt.show()
    