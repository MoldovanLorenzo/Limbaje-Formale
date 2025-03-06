

class MooreMachine:
    def __init__(self):

        self.states = {
            "S1": "O1",
            "S2": "O2"
        }

        self.transitions = {
            ("S1", "A"): "S1",
            ("S1", "B"): "S2",
            ("S2", "A"): "S1",
            ("S2", "B"): "S2"
        }

        self.current_state = "S1"

    def process_input(self, inputs):
        outputs = []
        for symbol in inputs:
            outputs.append(self.states[self.current_state])
            self.current_state = self.transitions.get((self.current_state, symbol), self.current_state)
        outputs.append(self.states[self.current_state])
        return outputs
machine = MooreMachine()
input_sequence = ["A", "B", "B", "A", "A", "B"]
output_sequence = machine.process_input(input_sequence)

print("Input Sequence: ", input_sequence)
print("Output Sequence:", output_sequence)
