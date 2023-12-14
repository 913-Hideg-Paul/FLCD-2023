from Grammar import Grammar
from Parser import RecursiveDescentParser

def main():
    # Create a Grammar object and read from a file
    grammar = Grammar()
    grammar.read_from_file("g1.in")

    # Create a RecursiveDescentParser object using the Grammar
    rd_parser = RecursiveDescentParser(grammar)

    # Parse an input string
    input_string = "abc"
    if rd_parser.parse_input(input_string):
        print("Parsing successful!")
    else:
        print("Parsing failed.")

if __name__ == "__main__":
    main()
