from Grammar import Grammar

class RecursiveDescentParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.input_string = ""
        self.index = 0

    def expand(self, non_terminal):
        if non_terminal in self.grammar.P:
            for production in self.grammar.P[non_terminal]:
                self.grammar.P[non_terminal] = production
                self.index = 0
                if self.another_try():
                    return True
        return False

    def advance(self):
        self.index += 1

    def momentary_insuccess(self):
        self.grammar.P[self.grammar.S] = [[self.grammar.S]]
        self.index = 0

    def back(self):
        self.index -= 1

    def another_try(self):
        return self.parse()

    def success(self):
        return self.index == len(self.input_string)

    def parse(self):
        current_symbol = self.grammar.P[self.grammar.S][self.index]

        if current_symbol in self.grammar.N:
            if not self.expand(current_symbol):
                return False
        elif current_symbol in self.grammar.E or current_symbol == Grammar.EPSILON:
            if current_symbol == self.input_string[self.index]:
                self.advance()
            else:
                self.momentary_insuccess()
                return False
        else:
            return False

        return self.success()

    def parse_input(self, input_string):
        self.input_string = input_string
        self.index = 0
        return self.parse()
