
# Little Man Computer in Python

List of instructions of LMC 

* ADD - 1XX - acc <- acc + mem[xx] 
* SUB - 2XX - acc <- acc +  mem[xx] 
* STA - 3XX - mem[xx] <- acc 
* LDA - 5XX - acc <-  mem[xx] 
* BRA - 6XX - pc <- xx 
* BRZ - 7XX - if acc == 0 then pc <- xx 
* BRP - 8XX - if acc >= 0 then pc <- xx 
* INP - 901 - acc <- Input 
* INP - 902 - acc -> Output 
* HLT - 000 - Halts the machine
* DAT       - Assembler directive to store data into a memory location
* Other than intructions all are treated as Labels

Run:

```bash
$ python LMC.py paths
```

Example:

```bash
$ python LMC.py path1.lmc path2.lmc
```

