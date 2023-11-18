// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(LOOP)
    @SCREEN
    D=A
    @address
    M=D

    @KBD
    D=M
    @FILL
    D;JNE

(EMPTY)
    @address
    A=M
    M=0

    @address
    D=M
    @KBD
    D=D-A
    D=D+1
    @LOOP
    D;JEQ

    @address
    M=M+1
    @EMPTY
    0;JMP

(FILL)
    @address
    A=M
    M=-1

    @address
    D=M
    @KBD
    D=D-A
    D=D+1
    @LOOP
    D;JEQ

    @address
    M=M+1
    @FILL
    0;JMP
