from BasicInterpreter import Interpreter
from sys import argv

if __name__ == "__main__":
    interpreter = Interpreter()
    interpreter.interpret(argv[1])