class AutomatCafea:
    def __init__(self):
        self.stare = "q0"

    def tranzitie(self, input):
        tranzitii = {
            ("q0", "C"): "q1", ("q0", "T"): "q2", ("q0", "A"): "q3", ("q0", "H"): "q4",
            ("q1", "OK"): "q4", ("q2", "OK"): "q4", ("q3", "OK"): "q4", ("q4", "OK"): "q0"
        }

        if (self.stare, input) in tranzitii:
            self.stare = tranzitii[(self.stare, input)]
        else:
            print("Intrare invalida")

    def ruleaza(self):
        while True:
            print(f"Stare curenta: {self.stare}")
            if self.stare == "q4":
                print("Bautura a fost preparata. Puteti selecta alta.")
            input_utilizator = input("Introduceți C (cafea), T (ceai), A (capucino), H (ciocolata calda) sau OK: ")
            self.tranzitie(input_utilizator)

            if input_utilizator == "exit":
                break


if __name__ == "__main__":
    automat = AutomatCafea()
    automat.ruleaza()
