
import os
from Code import Code
from Parser import Parser

def AssemberNoSymbol(input_file_path, output_file_name):
        
    parser = Parser(input_file_path)
    code = Code()

    # Create an output file for the generated machine code
    output_file = open(os.path.join("/Users/yan/Desktop/nand2teris/projects/06/", output_file_name), "w")

    # Process each line of the assembly code
    while parser.hasMoreCommands():
        parser.advance()
        
        # Determine the command type
        command_type = parser.commandType()
        
        if command_type == "A_COMMAND":
            symbol = parser.symbol()
            # Generate binary code for A-command and write it to the output file
            binary_code = "0" + bin(int(symbol))[2:].zfill(15) + "\n"
            output_file.write(binary_code)
        elif command_type == "C_COMMAND":
            dest = parser.dest()
            comp = parser.comp()
            jump = parser.jump()
            # Generate binary code for C-command and write it to the output file
            binary_code = "111" + code.comp(comp) + code.dest(dest) + code.jump(jump) + "\n"
            output_file.write(binary_code)

    # Close the output file
    output_file.close()
    
def main():
    AssemberNoSymbol("/Users/yan/Desktop/nand2teris/projects/06/add/Add.asm", "Add.hack")
    AssemberNoSymbol("/Users/yan/Desktop/nand2teris/projects/06/pong/PongL.asm", "PongL.hack")
    AssemberNoSymbol("/Users/yan/Desktop/nand2teris/projects/06/rect/RectL.asm", "RectL.hack")
    
if __name__ == "__main__":
    main()