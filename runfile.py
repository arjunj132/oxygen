from oxygen import Oxygen
import sys
import os

cwd = os.getcwd()

f = open(cwd + "/" + sys.argv[1], "r")

oxygen = Oxygen("\n" + f.read() + "\n")

result = oxygen.lexer()
# Uncomment to recive lexer info
#print(result)
if result["error"] != False:
    print("Lexer: " + result["error"])
    sys.exit()
oxygen.parse(result["tokens"])