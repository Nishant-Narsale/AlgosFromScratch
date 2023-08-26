import numpy as np
import pandas as pd
from activationFunctions import relu


class Layer:
    def __init__(self, *args, **kwargs):
        self.num_of_neurons = kwargs["neurons"]
        self.last_layer_neurons = kwargs["last_layer_neurons"]
        self.weights = np.random.uniform(low=-0.5, high=0.5, size=(self.num_of_neurons,self.last_layer_neurons))  #between -0.5 and 0.5
        self.bias = np.random.uniform(low=-0.5, high=0.5, size=(self.num_of_neurons, 1))
        self.activation_function = kwargs["activation_function"]


class NeuralNetwork:
    def __init__(self, *args, **kwargs) -> None:
        self.layers = []
        self.activation_function = "relu"
        self.last_layer_neurons = kwargs["input_size"][1]
        if "default_activation_function" in kwargs:
            self.activation_function = kwargs["default_activation_function"]
        print("[INFO] default activation function for all the layers is set to", self.activation_function)
        

    def fit(self, X, y):
        pass
    
    def add(self, **kwargs):
        if "neurons" in kwargs:
            if "activation_function" in kwargs:
                self.activation_function = kwargs["activation_function"]
            layer = Layer(neurons=kwargs["neurons"], activation_function=self.activation_function, last_layer_neurons=self.last_layer_neurons)                
            self.layers.append(layer)
            self.last_layer_neurons = kwargs["neurons"]

        else:
            raise AttributeError("Number of neurons is not given")


nn = NeuralNetwork(default_activation_function="sigmoid", input_size=(41000, 784))
nn.add(neurons=5, activation_function="relu")
nn.add(neurons=1, activation_function="sigmoid")