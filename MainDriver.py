from TestDriver import *
from utils      import *
from Lexer      import *
from Assembler  import *
from VM         import *

class MainDriver():
	def __execute(self,paths = []):
		if len(paths) != 0:
			for path in paths:
				print('Executing file: {}'.format(path))
				source = file_get_contents(path)
				program = Assembler(Lexer(source).lex()).assemble()
				vObj    = VM(program)  
				vObj.run()	
				print()
				
	def main(self,argv = []):
		if len(argv) > 1:
			if argv[1] == '-test':
				TestDriver().run()
			else:	
				paths = argv[1:]
				paths = list(filter(lambda file : file_exists(file),paths))
				self.__execute(paths)
