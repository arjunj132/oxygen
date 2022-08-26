G='error'
F='\n'
C=print
from oxygen import Oxygen as D
import sys
C('Oxygen v1.0.0 [OxyParser, default]')
C('(c) Arjun J')
while True:
	try:
		E=input('>>> ');B=D(F+E+F);A=B.lexer()
		if A[G]!=False:C(A[G])
		B.parse(A['tokens'])
	except KeyboardInterrupt:sys.exit()
