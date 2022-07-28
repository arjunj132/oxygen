from oxygen import Oxygen
import sys

print("Oxygen v1.0.0 [OxyParser, default]")
print("(c) Arjun J")
while True:
    try:
        command = input(">>> ")
        oxygen = Oxygen("\n" + command + "\n")
        result = oxygen.lexer()
        # Uncomment to recive lexer info
        #print(result)
        if result["error"] != False:
            print(result["error"])
        oxygen.parse(result["tokens"])
    except KeyboardInterrupt:
        sys.exit()