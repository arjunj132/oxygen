G='error'
F='\n'
from oxygen import Oxygen as C
import sys,os
D=os.getcwd()
E=open(D+'/'+sys.argv[1],'r')
B=C(F+E.read()+F)
A=B.lexer()
if A[G]!=False:print('Lexer: '+A[G]);sys.exit()
B.parse(A['tokens'])
