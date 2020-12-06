ADD =   1
SUB =   2
LDA =   3
STA =   5
BRA =   6
BRZ =   7
BRP =   8
INP = 901
OUT = 902
HLT =   0

opcodes = {
	'HLT' :  {
		'opcode' : 0,
		'args'   : 0,
	},
	'ADD' :  {
		'opcode' : 1,
		'args'   : 1,
	},
	'SUB' :  {
		'opcode' : 2,
		'args'   : 1,
	},
	'LDA' :  {
		'opcode' : 3,
		'args'   : 1,
	},
	'STA' :  {
		'opcode' : 5,
		'args'   : 1,
	},
	'BRA' :  {
		'opcode' : 6,
		'args'   : 1,
	},
	'BRZ' :  {
		'opcode' : 7,
		'args'   : 1,
	},
	'BRP' :  {
		'opcode' : 8,
		'args'   : 1,
	},
	'INP' :  {
		'opcode' : 901,
		'args'   : 0,
	},
	'OUT' :  {
		'opcode' : 902,
		'args'   : 0,
	},
}






