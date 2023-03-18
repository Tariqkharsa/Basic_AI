# cost function C(xi, yi) = (yi - w*ti)^2
# Gradient/Derivative of cost function C(ti, yi) = 2*(yi - w*ti)*-1*ti
# w is weights/slopes/rate_of_change
# ti is time in seconds at index i
# yi is distance in meters at index i
# we know that distance = velcoity*time
# This means yi = w*ti, where w is the actual velocity of the object

# This algorithm is an approach of finding the average velocity of a data set using gradient descent (core of neural networks)

from numpy import random

def gradient_descent(t, y, w, data_length):
    learning_rate = 0.00001
    index = 0
    weight = w
    y_pred = weight*t[index]
    iteration = 0
    print(weight)
    while(iteration < data_length - 1):
        gradient = 2*(y[index] - y_pred)*-1*t[index]
        weight = weight - learning_rate*gradient
        index += 1
        y_pred = weight*t[index]
        iteration += 1
        print(weight)
       
# stores random data points for time
t = random.randint(100, size=(200))
# stores actual data points for distances based on time
y = []
actual_velocity = 20
for i in range(len(t)):
    y.append(actual_velocity*t[i])
# predicted velocity
pred_velocity = 50

len_t = len(t)

gradient_descent(t, y, pred_velocity, len_t)
