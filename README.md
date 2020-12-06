
# Little Man Computer in Python

List of instructions of LMC 

* ADD - 1XX - acc <- acc + mem[xx] 
* SUB - 2XX - acc <- acc -  mem[xx] 
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


Modern computers contain a processor which executes instructions and memory which stores both the instructions and also the data that is to be used. In addition there are various means both to give data to the computer and to receive information from it. Although The Little Man Computer is a simulation of how a computer works. It is a heavily simplified version of a computer from the one that sits on your desk but nonetheless it is an excellent tool to learn how a computer works. from You will recall that a computer has various components including means to input data, output information, carry out calculations and store results.



| Instruction        | Mnemonic | Machine Code  | Info                                                                                         | Example        |
|--------------------|----------|---------------|----------------------------------------------------------------------------------------------|----------------|
| End                | HLT      | 000           | Ends the program                                                                             | HLT            |
| Add                | ADD      | 1xx           | Adds the value at address xx to the accumulator                                              | ADD 50         |
| Subtract           | SUB      | 2xx           | Subtracts the value at address xx from accumulator                                           | SUB 50         |
| Store              | STA      | 3xx           | Storecontents of accumulator to address xx                                                   | STA 50         |
| Load               | LDA      | 5xx           | Loads contents of address xx to the accumulator                                              | LDA 50         |
| Branch Always      | BRA      | 6xx           | Jumps to the instruction at address xx                                                       | BRA 05         |
| Branch If Zero     | BRZ      | 7xx           | Jumps to the instruction at address xx, given the value  in the accumulator is 0             | BRZ 05         |
| Branch If Positive | BRP      | 8xx           | Jumps to the instruction at address xx, given the value  in the accumulator is 0, or greater | BRP 05         |
| Input              | INP      | 901           | Prompts user for input, store in accumulator                                                 | INP            |
| Output             | OUT      | 902           | Outputs value currently in accumulator                                                       | OUT            |
| Data               | DAT      | -             | Reserves a place in memory for a variable, followed by the initial value of said var         | VarName DAT 50 |


Run:

```bash
$ python LMC.py paths
```

Example:

```bash
$ python LMC.py path1.lmc path2.lmc
```

