class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
            self._change_state()

    def is_ripe(self):
        if self._state == 3:
         return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()
    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')