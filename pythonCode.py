from _csv import writer

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

 #Code for generating data points to plot output function y vs alpha_a corresponding to p=3pi/2



p=3*np.pi/2
x=[]                   #values for alpha_a
y=[]                   #values for function y

i=math.radians(-820)
while i<= math.radians(820):
    if i!=math.radians(0):
        x.append(i)
        y.append(np.sin(i)*(p/(i))+np.cos(i))
    else:
        x.append(i)
        y.append(np.sin(i)*(p/(i))  + np.cos(i))
    i=i+math.radians(0.8)

# plotting data for corresponding x and y

plt.plot(x,y)
plt.show()

#Creating .csv file

with open('mycsv.csv', 'w' , newline='') as f:
    fieldnames =['x_axis' , 'y_axis']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    thewriter.writeheader()
    for i in range(len(x)):
        thewriter.writerow({'x_axis' : x[i],'y_axis' : y[i]})

