from Opcode import *
 
class Assembler():
	'''Simple Three Pass Assembler'''	
	def __init__(self,tokens = []):
		self.__program  = []      ## hold the final bytecode or opcode after pass1,pass2 and pass3
		self.__tokens   = tokens  ## hold the tokens
		self.__labels   = {}      ## hold the labels (label : address)  
		self.__program_pass1 = [] ## hold the output of pass 1
		self.__program_pass2 = [] ## hold the output of pass 2
	
	def __lookahed_token(self,loc = 0):
		'''Look ahead of tokens'''
		if loc < len(self.__tokens):
			return self.__tokens[loc]
		else:
			return None
	
	def __lookahed_pass1(self,loc = 0):
		'''Look ahead of __program_pass1'''
		if loc < len(self.__program_pass1):
			return self.__program_pass1[loc]
		else:
			return None
			
	def __pass1(self):
		'''
		In this pass we try to assemble the instructions and operand into one unit.
		If the opreand is a label we store it as an list
		ex: ['LDA',7,'STA','one','hlt','one','dat',1]
		    [507,['sta','one'],000,'one','dat',1]
		'''
		loc = 0
		while loc < len(self.__tokens):
			token = self.__lookahed_token(loc)
			if token.type == 'INSTRUCTION':
				opcode = opcodes[token.value]['opcode']
				args   = opcodes[token.value]['args']
				if args > 0:
					i = loc + 1
					operands = []
					while i <= loc + args:
						next_token = self.__lookahed_token(i)
						operands.append(next_token)
						i = i + 1
					if operands[0].type == 'NUMBER':
						self.__program_pass1.append(opcode*100+operands[0].value)
					else:
						self.__program_pass1.append([opcode,operands[0]])
					loc = loc + args + 1
				else:
					self.__program_pass1.append(opcode)
					loc = loc + 1	
			else:
				self.__program_pass1.append(token)				
				loc = loc + 1

	def __pass2(self):
		'''
		In this pass we try to resolve the dat and store the addresses of labels.
		ex: ['LDA',7,'STA','one','hlt','one','dat',1]
		    [507,['sta','one'],000,1]
			{'one' : 3}
		'''
		loc = 0 
		pc  = 0
		while loc < len(self.__program_pass1):
			token = self.__lookahed_pass1(loc)
			if isinstance(token,list):
				self.__program_pass2.append(token)				
				loc = loc + 1
				pc  = pc  + 1
			elif isinstance(token,int):
				self.__program_pass2.append(token)				
				loc = loc + 1
				pc  = pc  + 1
			else:
				if token.type == 'DIRECTIVE':
					next_token = self.__lookahed_pass1(loc+1)
					val = 0
					if next_token != None:
						if next_token.type == 'NUMBER':
							val = next_token.value
					self.__program_pass2.append(val)				
					pc  = pc  + 1
				elif token.type == 'LABEL':
					label = token.value
					if label not in self.__labels: 
						self.__labels[token.value] = pc
					else:
						raise Exception('LABEL: {} already exists'.format(label))
				loc = loc + 1
	
	def __pass3(self):
		'''
		In this pass we try to resolve labels.
		ex: ['LDA',7,'STA','one','hlt','one','dat',1]
		    [507,303,000,1]
			{'one' : 3}
		'''
		loc = 0
		while loc < len(self.__program_pass2):
			token = self.__program_pass2[loc]
			if isinstance(token,list):
				label = token[1].value
				if label in self.__labels: 
					addr = self.__labels[label]
					if addr >= 0 and addr <= 99:
						self.__program.append(token[0] * 100 + addr)
					else:	
						raise Exception('INVALID ADDRESS: {}'.format(addr))
				else:
					raise Exception('INVALID LABEL: {}'.format(label))
			else:
				self.__program.append(token)
			loc = loc + 1
	
	def assemble(self):	
		self.__pass1()
		self.__pass2()
		self.__pass3()
		return self.__program
