from Opcode import *

class VM():
	'''Little Man Computer Virtual Machine'''
	def __init__(self,code = []):
		self.__code = code ## Compiled Code
		self.__pc   = 0    ## Program Countr
		self.__acc  = 0    ## Accumalator 
		
		self.__mem  = [0 for index in range(100)] ## Memory or Mailbox
		
		self.__is_running = False
		
		## Loading code into our memory 
		addr = 0
		while addr < len(code):
			self.__set_mem(addr,code[addr])
			addr = addr + 1
			
	def __set_mem(self,addr = 0,value = 0):
		'''Used for setting a value to a memory location'''
		if addr >= 0 and addr <= len(self.__mem)-1:
			self.__mem[addr] = value 
	
	def __get_mem(self,addr = 0):
		'''Used for getting a value from a memory location'''
		if addr >= 0 and addr <= len(self.__mem)-1:
			value = self.__mem[addr]
			return value
	
	def get_mem(self,addr = 0):
		'''Used for getting a value from a memory location'''
		return self.__get_mem(addr)
	
	def get_acc(self):
		'''Used for getting the value of accumalator'''
		return self.__acc
		
	def __step(self):
		'''Used for excuting or stepping through intructions'''
		instruction = self.__get_mem(self.__pc) ## current instruction 
		self.__pc = self.__pc + 1               ## increment the program counter 
		
		if instruction == HLT:    ## Halts the program
			self.__is_running = False
		elif instruction == INP:  ## Input a number to accumalator
			self.__acc = int(input('Enter a number in acc: '))
		elif instruction == OUT:  ## Output the value of the accumalator
			print('{}'.format(self.__acc))
		else:
			opcode = int(instruction / 100) ## Decode the opcode
			addr   = int(instruction % 100) ## Decode the operand which is an address
			if opcode == ADD:     ## Add the value from memory address to the accumalator
				self.__acc = self.__acc + self.__get_mem(addr)
			elif opcode == SUB:   ## Subtract the value from memory address from the accumalator
				self.__acc = self.__acc - self.__get_mem(addr)
			elif opcode == LDA:   ## Load the value from memory address to the accumalator
				self.__acc = self.__get_mem(addr)
			elif opcode == STA:   ## Store the value of the accumalator to the memory address
				self.__set_mem(addr,self.__acc)
			elif opcode == BRA:   ## Set the pc to the addrress
				self.__pc = addr
			elif opcode == BRZ:   ## If valure of the accumalator is 0 then Set the pc to the address
				if self.__acc == 0:
					self.__pc = addr
			elif opcode == BRP:   ## If valure of the accumalator is Positive then Set the pc to the address
				if self.__acc >= 0:
					self.__pc = addr
			else:                 ## Invalid Opcode
				raise Exception('INVALID OPCODE: {}'.format(opcode))
	
	def run(self):
		'''Run the program'''
		self.__is_running = True
		while self.__is_running and self.__pc < len(self.__code):
			self.__step()


