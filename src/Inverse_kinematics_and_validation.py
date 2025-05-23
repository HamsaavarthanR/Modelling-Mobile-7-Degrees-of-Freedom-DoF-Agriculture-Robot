# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O05RJlKwrnP-Tko7qZ8NbaFGUzKPxkOk
"""

### Inverse Kinematics ###

## Obtain Velocity Kinematics Eqn.: LINEAR Jacobian Matrix (Jv) ##

import sympy as sp
import math
import numpy as np
from sympy import *
from sympy import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


## Define the joint anlges which are function of time
θ1, θ2, θ3, θ4, t = sp.symbols('θ1 θ2 θ3 θ4 t')

## Home Posititon
# θ1 = 0
# θ2 = 0
# θ3 = 0
# θ4 = 0

## Define the DH Table (Matrix: [a_i, alpha_i, d_i, theta_i])
DH = sp.Matrix([[0,  sp.rad(-90), 9.15, θ1],
                [-6, sp.rad(180), 0,    sp.rad(90)+θ2],
                [6,  0,           0,    sp.rad(90)+θ3],
                [2,  0,           0,    θ4]])


## Initiate a list to store all the homogeneous transofrmation matrices
H = []

for i in range(DH.shape[0]):
    ## Calculate Transformation Matrix at each frame using the DH Table
    T = sp.Matrix([[sp.cos(DH[i, 3]), -sp.sin(DH[i, 3])*sp.cos(DH[i, 1]),sp.sin(DH[i, 3])*sp.sin(DH[i, 1]), sp.cos(DH[i, 3])*DH[i, 0]],
                     [sp.sin(DH[i, 3]), sp.cos(DH[i, 3])*sp.cos(DH[i, 1]), -sp.cos(DH[i, 3])*sp.sin(DH[i, 1]), sp.sin(DH[i, 3])*DH[i, 0]],
                      [0, sp.sin(DH[i, 1]), sp.cos(DH[i, 1]), DH[i, 2]],
                       [0, 0, 0, 1]])

    ## Store the matrix in 'H'
    H.append(T)

## Initiate Identity matrix to start the matrix multiplication to obtain final Homo. Trans. Mat.
Final = identity_matrix = np.identity(4, dtype="int")

## Inittiate list to store Trans. Matrices for frame 'n' w.r.t frame '0', n=1,2,3,4..
T0_n = []

Base_transforms = []

for i in range(DH.shape[0]):
    Final = Final*H[i]
    T0_n.append(Final)

# T0_n[0] = T1 = H[0]
# T0_n[1] = T1*T2 = H[0]*H[1]
# T0_n[2] = T1*T2*T3 = H[0]*H[1]*H[2]
# T0_n[3] = T1*T2*T3*T4 = H[0]*H[1]*H[2]*H[3]


## End-effector position coordinates (x, y, z) wrt base frame
p = []
p.append(Final[0, 3])
p.append(Final[1, 3])
p.append(Final[2, 3])
# print(p)

## Now, compute the LINEAR Velocity Jacobian Matrix (Jv) using method 2 (using z-components and partial derivatives): First 3 rows (Upper-half) of Overall Jacobian Matrix (J)
# j'th column of Jv = d(O_0n)/dqj, for revolute joint qj = theta_j and O_0n => Position of enf-effector(n) w.r.t base frame(0)
# Jv[i][j] = d(O_0n[i])/dθj
Jv = sp.Matrix([[sp.diff(p[0], θ1), sp.diff(p[0], θ2), sp.diff(p[0], θ3),sp.diff(p[0], θ4)],
                    [sp.diff(p[1], θ1), sp.diff(p[1], θ2), sp.diff(p[1], θ3),sp.diff(p[1], θ4)],
                    [sp.diff(p[2], θ1), sp.diff(p[2], θ2), sp.diff(p[2], θ3),sp.diff(p[2], θ4)]])

print("Linear Velocity Jacobian Matrix (Jv) for given Robot Arm:")
pprint(Jv)


## Rank of Jv (3*4)
# pprint(Jv)
print("The Rank of a Matrix: ", Jv.rank())


## Geometric Validation


## Initial Joint variable values
t1=0.00
t2=0.00
t3=0.00
t4=0.00

t=0
dt = 0.1

## Total time extimated to complete the trajectory (Less than 20 seconds)
T = 10

## Initiate list to store end-effector coordinates
X = []
Y = []
Z = []

## loop for itereating over the time elapsed
while t <= T:

    ## Substitute angle values into the Jacobian (Jv)
    Jv_subs = Jv.subs([(θ1,t1),(θ2,t2),(θ3,t3),(θ4,t4)])

    ## Since Jv is (3*4), not n*n, Jv Inverse can't be directly computed from Jv inversion
    ## Have to compute the 'Right Pseudoinverse' of Jv

    ## Check if (Jv*Jv_T) Inverse exists
    # Condition: (Jv*Jv_T) Inverse exists for Jv (m*n), if m < n and rank Jv = m
    # Fomr the previous cell, we already know that Rank of Jv (3*4) = 3
    # Therfore, (Jv*Jv_T) Inverse exists

    ## Compute Right Pseudoinverse of Jv_subs
    # J_plus = J_T(JJ_T)-1
    Jv_T = Jv_subs.T
    Jv_right_pseudo = Jv_T * (Jv_subs * Jv_T).inv()

    ## Therefore, q_dot = Jv_right_pseudo * X_dot, where X_dot = (x_dot, y_dot, z_dot), NOTE: w_x, w_y, w_z not considered in this case


    ## Now, Compute Velocity Trajectory (X_dot)
    ## Line equation to connect the home-position of end-effector and target coordinates

    # ## Circle fot time t = 0 to t = T
    X_dot = Matrix([[0],
                    [((4/T)*math.pi) * sin((math.pi/2) + (((2*math.pi)/T)*t))],
                    [((4/T)*math.pi) * cos((math.pi/2) + ((2*math.pi)/T)*t)]])



    ## Line Eqn. from home position to target position (12, 4, 19.15) w.r.t base frame (0)
    # X_dot = Matrix([[2/T],
    #                 [2/T],
    #                 [2/T]])

    ## Compute Joint Velocities
    q_dot = Jv_right_pseudo * X_dot

    ## Extract the joint velocities
    q1_dot = q_dot[0,0]
    q2_dot = q_dot[1,0]
    q3_dot = q_dot[2,0]
    q4_dot = q_dot[3,0]

    ## Compute Joint Angles
    q1 = t1 + (q1_dot * dt)
    q2 = t2 + (q2_dot * dt)
    q3 = t3 + (q3_dot * dt)
    q4 = t4 + (q4_dot * dt)

    ## Substitude the new joint angles in the Final Transformation Matrix
    T_end = Final.subs([(θ1,q1),(θ2,q2),(θ3,q3),(θ4,q4)])

    ## Extracting Position values of the end effector wrt base
    x = T_end[0,3]
    y = T_end[1,3]
    z = T_end[2,3]

    ## Store the coordinates of end-effector (x, y, z)
    X.append(x)
    Y.append(y)
    Z.append(z)

    ## Update values for next iteration
    t1 = q1
    t2 = q2
    t3 = q3
    t4 = q4

    ## Update time (t)
    t = t + dt


## 2D plot of the trajectory
fig, ax = plt.subplots()
plt.plot(Y, Z)
ax.set_aspect('equal')
plt.title('Trajectory Path Plot')
plt.xlabel('Y-axis')
plt.ylabel('Z-axis')
plt.show()


## 3D plot of the Trajectory
fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(X, Y, Z, color='b', linewidths=0.1)
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.set_zlabel('Z-axis')
ax1.set_xlim3d(0, 10)