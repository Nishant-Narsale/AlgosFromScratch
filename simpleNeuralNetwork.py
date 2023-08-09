class NeuralNetwork:
    def __init__(self, *args, **kwargs) -> None:
        self.layers = []

    def fit(self, X, y):
        pass
    
    def add(self, **kwargs):
        try:
            print(kwargs["neurons"])
        except:
            raise AttributeError("Number of neurons is not given")


nn = NeuralNetwork(default_activation_function="sigmoid")
nn.add()
nn.add(neurons=5, activation_function="relu")
nn.add(neurons=1, activation_function="sigmoid")