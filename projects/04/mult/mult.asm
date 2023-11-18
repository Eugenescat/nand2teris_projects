// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// Assumes that R0 >= 0, R1 >= 0, and R0 * R1 < 32768.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)


// sum=0
// for (i=0; i<RAM[1]; i++):
//     sum = sum + RAM[0]
// RAM[2] = sum

@i
M=0
@sum
M=0

(LOOP)
@R1
D=M
@i
D=D-M
@STORE
D;JEQ

@sum
D=M
@R0
D=D+M
@sum
M=D
@i
M=M+1
@LOOP
0;JMP

(STORE)
@sum
D=M
@R2
M=D

(END)
@END
0;JMP

