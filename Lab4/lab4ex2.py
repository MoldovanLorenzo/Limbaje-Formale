class MealyMachine:
    def __init__(self):

        self.transitions = {
            ("Q1", "X"): ("Q2", "O1"),
            ("Q1", "Y"): ("Q1", "O1"),
            ("Q2", "X"): ("Q1", "O2"),
            ("Q2", "Y"): ("Q2", "O2")
        }

        self.current_state = "Q1"

    def process_input(self, inputs):
        outputs = []
        for symbol in inputs:

            self.current_state, output = self.transitions.get((self.current_state, symbol), (self.current_state, None))
            outputs.append(output)
        return outputs


machine = MealyMachine()
input_sequence = ["X", "Y", "X", "X", "Y"]
output_sequence = machine.process_input(input_sequence)

print("Input : ", input_sequence)
print("Output :", output_sequence)
