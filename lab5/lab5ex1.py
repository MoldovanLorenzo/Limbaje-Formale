class MealyMachine:
    def __init__(self):
        self.state = "S0"


        self.transitions = {
            ("S0", (0, 0)): "S0",
            ("S0", (0, 1)): "S1",
            ("S0", (1, 0)): "S0",
            ("S0", (1, 1)): "S1",
            ("S1", (0, 0)): "S0",
            ("S1", (0, 1)): "S1",
            ("S1", (1, 0)): "S1",
            ("S1", (1, 1)): "S0",
        }


        self.outputs = {
            "S0": 0,
            "S1": 1
        }

    def process(self, inputs):

        outputs = [self.outputs[self.state]]
        for inp in inputs:
            self.state = self.transitions[(self.state, inp)]
            outputs.append(self.outputs[self.state])
        return outputs


moore = MealyMachine()
inputs = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0), (1, 0)]
outputs = moore.process(inputs)
print(" Output:", outputs)
