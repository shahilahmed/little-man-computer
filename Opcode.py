ADD =   1
SUB =   2
STA =   3
LDA =   5
BRA =   6
BRZ =   7
BRP =   8
INP = 901
OUT = 902
HLT =   0

opcodes = {
	'HLT' :  {
		'opcode' : HLT,
		'args'   : 0,
	},
	'ADD' :  {
		'opcode' : ADD,
		'args'   : 1,
	},
	'SUB' :  {
		'opcode' : SUB,
		'args'   : 1,
	},
	'STA' :  {
		'opcode' : STA,
		'args'   : 1,
	},
	'LDA' :  {
		'opcode' : LDA,
		'args'   : 1,
	},
	'BRA' :  {
		'opcode' : BRA,
		'args'   : 1,
	},
	'BRZ' :  {
		'opcode' : BRZ,
		'args'   : 1,
	},
	'BRP' :  {
		'opcode' : BRP,
		'args'   : 1,
	},
	'INP' :  {
		'opcode' : INP,
		'args'   : 0,
	},
	'OUT' :  {
		'opcode' : OUT,
		'args'   : 0,
	},
}






