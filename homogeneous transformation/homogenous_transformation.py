import math
import numpy as np

# Roarrtion and Transition of the drone
roll = 30
pitch = 20
yaw = 10
dx,dy,dz = 5,6,7


yawMatrix = np.matrix([[math.cos(math.radians(yaw)), -math.sin(math.radians(yaw)), 0],
                       [math.sin(math.radians(yaw)), math.cos(math.radians(yaw)), 0],
                       [0, 0, 1]])

pitchMatrix = np.matrix([[math.cos(math.radians(pitch)), 0, math.sin(math.radians(pitch))],
                         [0, 1, 0],
                         [-math.sin(math.radians(pitch)), 0, math.cos(math.radians(pitch))]])

rollMatrix = np.matrix([[1, 0, 0],
                        [0, math.cos(math.radians(roll)), -math.sin(math.radians(roll))],
                        [0, math.sin(math.radians(roll)), math.cos(math.radians(roll))]])

# Rotation Matrix
R = yawMatrix @pitchMatrix @ rollMatrix
R = (np.round(R, decimals=2)) 
print("Rotation Matrix" ,R)

# Homogenous Matrix
H =np.matrix([[R[0][0],R[0][1],R[0][2],dx],
              [R[1][0],R[1][1],R[1][2],dy],
              [R[2][0],R[2][1],R[2][2],dz],
              [0,0,0,1]])
H = (np.round(H, decimals=2)) 
print("Homogenous Matrix" ,H)

# Matrix for the circle
A =np.matrix([[1, 0, 0, 0,], 
              [0, 1, 0, 0],
              [0, 0, -1, 0],
              [0, 0, 0, 0]])

# Transpose of the Homogenous Matrix
HT = np.transpose(H)

# Matrix of the ellipse according to the world frame
B = HT@A@H

E = (np.delete(B, 2, 0))
E = (np.delete(E, 2, 1))

# Area Calculation
det = np.linalg.det(E)
E = np.array(E)

a = float(E[0][0])
b = float(E[0][1])
c =float( E[1][1])

num = -(math.pi)

den = ((a*c-(b**2))**(3/2))

# Area of the Ellipse
Area = (num/den)*det
Area = (np.round(Area, decimals=2)) 
print("Area of an ellipse", Area)



