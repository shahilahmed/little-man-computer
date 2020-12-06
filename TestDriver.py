from Lexer     import *
from Assembler import *
from VM        import *

class TestDriver():
	
	def __test_execute(self,source = ''):
		if len(source) != 0:
			program = Assembler(Lexer(source).lex()).assemble()
			vObj    = VM(program)  
			vObj.run()
			return vObj
		else:
			raise Exception('SOURCE CANNOT BE EMPTY DURING TEST EXCEUTE')
	
	@staticmethod		
	def __test_assert(cond = False,message = ''):
		if len(message) != 0:
			if cond == True:
				print('TEST PASSED: {}'.format(message))
			else:	
				raise Exception('TEST FAILED: {}'.format(message))
	
	def __test1(self):
		source = '''
				lda one
				hlt
		  one dat 1	
		'''
		vObj = self.__test_execute(source)
		TestDriver.__test_assert(vObj.get_acc() == 1,'[TEST 1] - Excepted 1 in the accumalator')
	
	def __test2(self):
		source = '''
				lda num
				sta 45
				hlt
		  num dat 67	
		'''
		vObj = self.__test_execute(source)
		TestDriver.__test_assert(vObj.get_mem(45) == 67,'[TEST 2] - Excepted 67 in the memory location 45')
	
	def __test3(self):
		source = '''
			lda first   ## load the first number into the accumalator
			add second  ## add the value of second number with accumalator
			sta result  ## store the value of the accumalator into result
			hlt         ## halt the machine
			first  dat 45
			second dat 45
			result dat 
		'''
		vObj = self.__test_execute(source)
		TestDriver.__test_assert(vObj.get_acc() == 90,'[TEST 3] - Excepted 90 in the accumalator')
	
	def __test4(self):
		source = '''
			loop
				lda n
				brz exit
				sub one
				sta n
				bra loop
			exit	
				hlt
			n dat 5
		  one dat 1	
		'''
		vObj = self.__test_execute(source)
		TestDriver.__test_assert(vObj.get_acc() == 0,'[TEST 4] - Excepted 0 in the accumalator')
	
	def __test5(self):
		source = '''
			loop
				lda n
				brz exit
				lda res
				add n
				sta res
				lda n
				sub one
				sta n
				bra loop
			exit
				lda res
				hlt
			n dat 10
		  one dat 1
		  res dat	
		'''
		vObj = self.__test_execute(source)
		TestDriver.__test_assert(vObj.get_acc() == 55,'[TEST 5] - Excepted 55 in the accumalator')
	
	def run(self):
		print('Running all the tests')
		self.__test1()
		self.__test2()
		self.__test3()
		self.__test4()
		self.__test5()
		print('Completed all the tests')
