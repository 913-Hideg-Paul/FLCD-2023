class Grammar:
    EPSILON = "epsilon"
    STARTING_SYMBOL = "S'"

    def __init__(self, is_enhanced=False):
        self.N = []
        self.E = []
        self.S = ""
        self.P = {}
        self.is_enhanced = is_enhanced

    def check_if_grammar_is_enhanced(self):
        if len(self.P[self.S]) != 1:
            return False
        for production in self.P.values():
            for rhs in production:
                if self.S in rhs:
                    return False
        return True

    def make_enhanced_grammar(self):
        if not self.is_enhanced:
            self.N.append(Grammar.STARTING_SYMBOL)
            self.P[Grammar.STARTING_SYMBOL] = [[self.S]]
            self.S = Grammar.STARTING_SYMBOL
            self.is_enhanced = True

    @staticmethod
    def __process_line(line: str):
        return line.strip().split(' ')[2:]

    def read_from_file(self, file_name: str):
        with open(file_name) as file:
            N = self.__process_line(file.readline())
            E = self.__process_line(file.readline())
            S = self.__process_line(file.readline())[0]

            file.readline()  # P =
            P = {}
            for line in file:
                split = line.strip().split('->')
                source = split[0].strip()
                sequence = split[1].lstrip(' ')
                sequence_list = []
                for c in sequence.split(' '):
                    sequence_list.append(c)

                if source in P.keys():
                    P[source].append(sequence_list)
                else:
                    P[source] = [sequence_list]

            self.N = N
            self.E = E
            self.S = S
            self.P = P

    def check_cfg(self):
        has_starting_symbol = False
        for key in self.P.keys():
            if key == self.S:
                has_starting_symbol = True
            if key not in self.N:
                return False
        if not has_starting_symbol:
            return False
        for production in self.P.values():
            for rhs in production:
                for value in rhs:
                    if value not in self.N and value not in self.E and value != Grammar.EPSILON:
                        return False
        return True

    def __str__(self):
        result = "N = " + str(self.N) + "\n"
        result += "E = " + str(self.E) + "\n"
        result += "S = " + str(self.S) + "\n"
        result += "P = " + str(self.P) + "\n"
        return result
