from Token import *
from Opcode import *

class Lexer():
	
	def __init__(self,source = ''):
		source = source + '\n'
		self.__source = source
		self.__tokens = []
		
		self.__pos  = 0
		self.__len  = len(self.__source)
		self.__line = 0
		self.__col  = 0
		
	def __is_eof(self):
		return not self.__pos < self.__len
	
	def __char(self):
		if not self.__is_eof():
			return self.__source[self.__pos]
		else:
			raise Exception('REACHED END OF FILE')
			
	def __next(self):		
		if not self.__is_eof():
			self.__pos =  self.__pos + 1
		else:
			raise Exception('REACHED END OF FILE')
	
	def __match(self,c = ''):
		if self.__char() == c:
			self.__next()
		else:
			raise Exception('excepted {} but found {}'.format(self.__char(),c))
	
	def __read_comment(self):
		if self.__char() == '#':
			self.__match('#')
			while not self.__is_eof() and self.__char() != '\n':
				self.__next()
		elif self.__char() == '[':
			self.__match('[')
			while not self.__is_eof() and self.__char() != ']':
				self.__next()
			self.__match(']')
			self.__match('#')
		else:
			raise Exception('excepted # or [ but found {}'.format(self.__char()))
	
	
	def __read_number(self):
		result = ''
		has_dot = 0
		while not self.__is_eof() and self.__char().isdigit() or self.__char() == '.':
			if self.__char() == '.':
				has_dot = has_dot + 1
				if has_dot > 1:
					break
			result = result + self.__char()
			self.__next()
		if has_dot > 1:	
			raise Exception('NUMBER CAN HAVE ONLY ONE DOT OR FLOATING POINT')
		if has_dot == 0:
			result = int(result)
		else:
			result = float(result)
		return Token('NUMBER',result)	
	
	def __read_symbol(self):
		result = ''
		while not self.__is_eof() and self.__char().isalpha() or self.__char().isdigit() or self.__char() == '_':
			result = result + self.__char()
			self.__next()
		if result.upper() in ['LABEL','DAT']:
			result = Token('DIRECTIVE',result.upper())
		elif result.upper() in opcodes:
			result = Token('INSTRUCTION',result.upper())
		else:
			return Token('LABEL',result)
		return result	
		
	def __tokenize(self):
		while not self.__is_eof():
			if self.__char() == ' ' or self.__char() == '\t' or self.__char() == '\r' or self.__char() == '\n':
				self.__next()
			elif self.__char() == '#':
				self.__match('#')
				self.__read_comment()
			else:
				if self.__char().isdigit():
					self.__tokens.append(self.__read_number())
				elif self.__char().isalpha():
					self.__tokens.append(self.__read_symbol())
				else:
					raise Exception('UNKNOWN CHARACTER {}'.format(self.__char()))
		return self.__tokens
	
	def lex(self):
		return self.__tokenize()

