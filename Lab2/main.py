
#ex1

class AutomatFinit:
    def __init__(self):
        self.stare_curenta = 'q0'
        self.tranzitii = {
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q2', '1': 'q0'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q3', '1': 'q3'}
        }
        self.stare_finala = 'q3'

    def proceseaza_input(self, intrare):
        for simbol in intrare:
            if simbol in self.tranzitii[self.stare_curenta]:
                self.stare_curenta = self.tranzitii[self.stare_curenta][simbol]
            else:
                return False
        return self.stare_curenta == self.stare_finala


#ex2

class DetectareCat:
    def __init__(self):
        self.stare_curenta = 'q0'

        self.transitions = {
            'q0': {
                'c': 'q1',
                'a': 'q0', 'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0',
                'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0',
                'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0',
                'q': 'q0', 'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0',
                'v': 'q0', 'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
            },
            'q1': {
                'a': 'q2',
                'c': 'q1',
                'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0', 'g': 'q0',
                'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0', 'l': 'q0',
                'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0', 'q': 'q0',
                'r': 'q0', 's': 'q0', 't': 'q0', 'u': 'q0', 'v': 'q0',
                'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
            },
            'q2': {
                't': 'q3',
                'c': 'q1',
                'a': 'q0', 'b': 'q0', 'd': 'q0', 'e': 'q0', 'f': 'q0',
                'g': 'q0', 'h': 'q0', 'i': 'q0', 'j': 'q0', 'k': 'q0',
                'l': 'q0', 'm': 'q0', 'n': 'q0', 'o': 'q0', 'p': 'q0',
                'q': 'q0', 'r': 'q0', 's': 'q0', 'u': 'q0', 'v': 'q0',
                'w': 'q0', 'x': 'q0', 'y': 'q0', 'z': 'q0'
            },
            'q3': {
                'a': 'q3', 'b': 'q3', 'd': 'q3', 'e': 'q3', 'f': 'q3',
                'g': 'q3', 'h': 'q3', 'i': 'q3', 'j': 'q3', 'k': 'q3',
                'l': 'q3', 'm': 'q3', 'n': 'q3', 'o': 'q3', 'p': 'q3',
                'q': 'q3', 'r': 'q3', 's': 'q3', 't': 'q3', 'u': 'q3',
                'v': 'q3', 'w': 'q3', 'x': 'q3', 'y': 'q3', 'z': 'q3'
            }
        }


        self.stare_finala = 'q3'

    def proceseaza_text(self, text):
        for caracter in text:

            if caracter in self.tranzitii[self.stare_curenta]:
                self.stare_curenta = self.tranzitii[self.stare_curenta][caracter]
            else:

                self.stare_curenta = 'q0'


            if self.stare_curenta == self.stare_finala:
                return True


        return False


#ex3
