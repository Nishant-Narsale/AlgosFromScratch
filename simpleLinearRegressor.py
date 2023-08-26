import numpy as np
import pandas as pd

class SimpleLinearRegressor:
    def __init__(self):
        """ 
        SimpleLinearRegressor is used to predict one dependent variable by training on one independent variable
        This class uses formulas to calculate best fit line

        Goal of SimpleLinearRegressor is to find a line which minimizes the Error function
        Error = Sum((actual - predicted)**2)
        At minima, derivative of error with respect to m and b is 0
        By solving further

        b = y[mean] - (m*x[mean])
        numerator = sum((x[i]-x[mean])*(y[i]-y[mean]))
        denominator = sum((x[i]-x[mean]**2))
        m = numerator/denominator

        """

        # A line is denoted by slope and y-intercept i.e., m and b
        self.m = None
        self.b = None 
        

    def fit(self, X_train, y_train):
        X_mean = X_train.mean()
        y_mean = y_train.mean()
        numerator = 0
        denominator = 0
        
        for i in range(len(X_train)):
            numerator += (X_train[i]-X_mean) * (y_train[i]-y_mean)
            denominator += (X_train[i]-X_mean)**2

        self.m = numerator/denominator
        self.b = y_mean - (self.m*X_mean)

        print(self.m, self.b)

    def predict(self, X_test):
        return self.m * X_test + self.b

