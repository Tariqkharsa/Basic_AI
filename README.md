# Gradient_Descent_Physics

In this repository, I will show you how gradient descent works for a basic physics probelm, especially for those who are new to the topic

The main idea behind Gradient Descent is to minimize the difference between the predicted and actual value.

Imagine a distance function that measures the difference between predicted and actual value. Such a function will look like this:
C(x) = (actual - predicted)^2 

The actual values are usually the observed value from an experiment. 
The predicted values are what we think the observed value should be (initially this could be any random value)

Now, what if there is a way we could find the local minimum of that function such that the difference between the actual and predicted values is almost zero. In that case, we have found an ideal way to generate a predicted value that is almost identical to the actual value.

The only problem is we don't have infinite data to see what the function or graph looks like. Therefore, we need to find a way to move toward that minimum by only using the given information. This is where gradient descent comes in. 

Gradient descent is the idea of taking the slope/derivative of a function at a single point, so that it results in a value that will tell us how to move towards a maximum. However, we could adjust that value by multiplying it by -1 to let us move in the direction of the local minimum. 

![image](https://user-images.githubusercontent.com/88465880/226085791-39a5628e-992c-4ee4-b216-d3b2f6d1a09a.png)
