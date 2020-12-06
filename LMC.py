from MainDriver import *
from sys import argv

class LMC():
	@staticmethod
	def main(argv = []):
		mDriver = MainDriver()
		mDriver.main(argv) 

if __name__ == '__main__':
	def info():
		__app_name__     = 'Little Man Computer'
		__app_version__  = 'v0.0.2'
		__app_author__   = 'Md Shahil Ahmed'
		print('{} {} by {}'.format(__app_name__,__app_version__,__app_author__))
		print()	
	try:
		info()
		if len(argv) == 1:
			print('usuage: python LMC.py paths')
		else:
			LMC.main(argv)
	except Exception as e:
		print(e)
