_R='tokens'
_Q='funcdef'
_P='funcname'
_O='functioncalled'
_N='print'
_M='num'
_L='op'
_K='importdef'
_J='run'
_I='import'
_H='function'
_G='nothing'
_F=False
_E='string'
_D='\n'
_C='keyword'
_B='type'
_A='value'
import sys,json,os
class Oxygen:
	def __init__(self,code):self.code=code
	def lexer(self):
		G=True;F='1234567890';E='';D='(';C='"';B=' ';A='error';code=self.code;length=len(code);pos=0;tokens=[{_B:_C,_A:_G}];custom_keywords=[];BUILT_IN_KEYWORDS=[_N,_H,_I,_G];chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_()""\',=-!@#$%^&*()\\{\\}|:"<>?,./~`;[]\\';mathoperators='+-/*%';allowedfunc=[];allowedkey=[]
		while pos<length:
			currentchar=code[pos]
			if currentchar==B or currentchar==_D:pos+=1
			elif currentchar==C:
				res=E;pos+=1
				while code[pos]!=C and code[pos]!=_D and pos<length:res+=code[pos];pos+=1
				if code[pos]!=C:return{A:'String does not end with "'}
				pos+=1;tokens.append({_B:_E,_A:res})
			elif currentchar in chars:
				res=currentchar;pos+=1;chars1=F
				if code[pos-1]==',':chars1+=B
				while code[pos]in chars+chars1 and code[pos]!=_D and code[pos]!='\r'and pos<length:res+=code[pos];pos+=1
				if res not in BUILT_IN_KEYWORDS:
					if tokens[len(tokens)-1][_A]!=_H:
						if res not in allowedfunc:
							works=_F
							for x in allowedkey:
								if res.split(D)[0]+D in x:works=G
							if res==')':works=G
							if works==_F:return{A:'Unexpected token "%s"'%res}
							else:tokens.append({_B:_J,_A:res})
						elif res in allowedfunc and res in allowedkey:print('Function and module both have the same value')
						elif res in allowedfunc:tokens.append({_B:_O,_A:res})
						else:
							for x in allowedkey:
								if res.split(D)[0]+D in x:tokens.append({_B:_J,_A:res})
					else:
						tokens.append({_B:_P,_A:res});allowedfunc.append(res)
						try:
							if code[pos+1]==B:pos+=1
						except:pass
						pos+=1;res=E
						try:
							while code[pos]!=':'and pos<length:res+=code[pos];pos+=1
						except:return{A:'Expected ":"'}
						pos+=1;tokens.append({_B:_Q,_A:res})
				else:
					tokens.append({_B:_C,_A:res})
					if res==_I:
						try:
							res=E
							if code[pos+1]==B:pos+=1
							pos+=2
							while code[pos]!=C and code[pos]!=_D and pos<length:res+=code[pos];pos+=1
							checkmodulecommands=open('opl/'+res+'/commands.json');x=checkmodulecommands.read();y=json.loads(x)
							for z in y:allowedkey.append(z)
							tokens.append({_B:_K,_A:res});pos+=1
						except Exception as e:return{A:'Could not import module: '+str(e)}
			elif currentchar in mathoperators:tokens.append({_B:_L,_A:currentchar});pos+=1
			elif currentchar in F:
				res=currentchar;pos+=1
				while code[pos]in'1234567890.'and pos<length:res+=code[pos];pos+=1
				tokens.append({_B:_M,_A:float(res)})
			else:return{A:'Unexpected character "%s"'%code[pos]}
		return{A:_F,_R:tokens}
	def parse(self,tokens):
		A='+';customfunc=[];functionvalue=[];commands=[];length=len(tokens);pos=0
		while pos<length:
			token=tokens[pos]
			if token[_B]==_C and token[_A]==_N:
				try:
					if tokens[pos+1]:0
				except:print('Unexpected end of line, expected string');sys.exit()
				isString=tokens[pos+1][_B]==_E
				if isString==_F:print('Unexpected token "'+tokens[pos+1][_A]+'", expected string');sys.exit()
				print(tokens[pos+1][_A]);pos+=2
			elif token[_B]==_L:
				try:
					if tokens[pos-1][_B]!=_E and tokens[pos-1][_B]!=_M:print('Expected type string or num, not '+tokens[pos-1][_B]);sys.exit()
					elif tokens[pos+1][_B]!=tokens[pos-1][_B]:print('Expected type '+tokens[pos-1][_B]+', not '+tokens[pos+1][_B]);sys.exit()
					elif tokens[pos+1][_B]==_E and token[_A]!=A:print('Cannot perform operation, string can only perform "+"');sys.exit()
					else:
						if tokens[pos+1][_B]==_E:res=tokens[pos-1][_A]+tokens[pos+1][_A];print(res)
						else:
							operation=token[_A]
							if operation==A:print(tokens[pos-1][_A]+tokens[pos+1][_A])
							if operation=='-':print(tokens[pos-1][_A]-tokens[pos+1][_A])
							if operation=='*':print(tokens[pos-1][_A]*tokens[pos+1][_A])
							if operation=='/':print(tokens[pos-1][_A]/tokens[pos+1][_A])
							if operation=='%':print(tokens[pos-1][_A]%tokens[pos+1][_A])
						pos+=2
				except:print('Can not find one of the one of the arguments required for performing the operation');sys.exit()
			elif token[_B]==_C and token[_A]==_H:
				if tokens[pos+1][_B]!=_P:print('Expected a function name, but instead got a '+tokens[pos+1][_B]);sys.exit()
				customfunc.append(tokens[pos+1][_A]);pos+=2
			elif token[_B]==_Q:functionvalue.append(token[_A]);pos+=1
			elif token[_A]in customfunc and token[_B]==_O:self.code=_D+functionvalue[customfunc.index(token[_A])]+_D;self.parse(self.lexer()[_R]);pos+=1
			elif token[_B]==_C and token[_A]==_I:
				if tokens[pos+1][_B]!=_K:print('Expected type importdef, but instead got '+tokens[pos+1][_B]);sys.exit()
				pos+=1
			elif token[_B]==_K:exec('from opl.'+token[_A]+'.run import *',globals(),locals());pos+=1
			elif token[_B]==_J:exec(token[_A],globals(),locals());pos+=1
			elif token[_B]==_E:pos+=1
			elif token[_B]==_M:
				try:
					if tokens[pos+1][_B]==_L:0
					else:print(token[_A])
				except:print(token[_A])
				pos+=1
			elif token[_B]==_C and token[_A]==_G:pos+=1
			else:print('Unexpected token '+token[_B]);sys.exit()
