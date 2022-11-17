import math
import numpy as np
import matplotlib.pyplot as plt

# Roarrtion and Transition of the drone
roll = 35
pitch = 15
yaw = 20
w_max = 1
roll_v = []
pitch_v = []
yaw_v = []



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

angle = ((((R[0][0]+R[1][1]+R[2][2]-1)/2)))
angle = ((180*(math.acos(angle)))/math.pi)

print("Angle of Rotation", angle)
axis = 1/(2*(math.sin(math.radians(angle))))
array = [(R[2][1]-R[1][2]),(R[0][2]-R[2][0]),(R[1][0]-R[0][1])]
array = (np.round(array, decimals=2)) 

axis = np.dot(axis,array)
print("Axis of Rotation",axis)

w = (w_max/np.max(axis))
print("magnitude of Velocity", w)

velocity_matrix = [w*axis[0],w*axis[1],w*axis[2]]
print("Velocity matrix",velocity_matrix)

T_min = angle/w
print("Minimum Time to reach the given orientation", T_min)

########################################################################################
# Plotting

T = int(np.round(T_min))
A = int(math.floor(angle))

x_vel = velocity_matrix[0]
x_v = []
for i in range(16):
    x_v.append(x_vel)
y_vel = velocity_matrix[1]
y_v = []
for i in range(16):
    y_v.append(y_vel)
z_vel = velocity_matrix[2]
z_v = []
for i in range(16):
    z_v.append(z_vel)

T = np.linspace(0,T,16)
A = np.linspace(0,A,16)
T = (np.round(T)) 
A = (np.round(A)) 




for angle in A:
 
    c = math.cos(math.radians(angle))
    s = math.sin(math.radians(angle))
    v = 1-c
    x = axis[0]
    y = axis[1]
    z = axis[2]
    
    
    Rotation_matrix = [[x*x*v+c,x*y*v-z*s,x*z*v+y*s],
                       [x*y*v+z*s,y*y*v+c,y*z*v-x*s],
                       [x*z*v-y*s,y*z*v+x*s,z*z*v+c]]
    
    R_M = (np.round(Rotation_matrix, decimals=2)) 
    
    
    roll = np.round(((180*(math.atan(R_M[2][1]/R_M[2][2])))/math.pi))
    roll_v.append(roll)
    
    
    
    pitch = np.round(((180*(math.atan((-R_M[2][0])/(math.sqrt((R_M[0][0]**2)+(R_M[1][0]**2))))))/math.pi))
    pitch_v.append(pitch)
    
    yaw = np.round(((180*(math.atan(R_M[1][0]/R_M[0][0])))/math.pi))
    yaw_v.append(yaw)
    
    


fig, (ax1, ax2,ax3,ax4,ax5,ax6) = plt.subplots(6,sharex=True,constrained_layout = True)
fig.suptitle('Plots of X velocity,Y velocity,Z velocity,X rotation,Y rotation,Z rotation with respect to Time respectivily')
ax1.plot(T,x_v)
ax2.plot(T,y_v)
ax3.plot(T,z_v)
ax4.plot(T,roll_v)
ax5.plot(T,pitch_v)
ax6.plot(T,yaw_v)




