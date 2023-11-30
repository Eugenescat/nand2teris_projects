
import os
from Code import Code
from Parser import Parser
from SymbolTable import SymbolTable

def Assember(input_file_path, output_file_name):
       
    parser_symbol_table = Parser(input_file_path)
    parser = Parser(input_file_path)
    code = Code()
    ram_table = SymbolTable()
    rom_table = SymbolTable()
    
    ram_table.map = {
             "SP": 0, "LCL":1, "ARG":2, "THIS":3, "THAT":4,
             "R0": 0, "R1":1, "R2":2, "R3":3, "R4":4, 
             "R5": 5, "R6":6, "R7":7, "R8":8, "R9":9,
             "R10":10, "R11":11, "R12":12, "R13":13, "R14":14,
             "R15":15, "SCREEN":16384, "KBD":24576
         }
    ram_table.address = 16

    # first pass
    while parser_symbol_table.hasMoreCommands():
        parser_symbol_table.advance()
        
        # Determine the command type
        command_type = parser_symbol_table.commandType()
        
        if command_type == "L_COMMAND":
            symbol = parser.symbol()
            rom_table.addEntry(symbol, rom_table.address)
        elif command_type == "A_COMMAND":
            rom_table.address += 1
        elif command_type == "C_COMMAND":
            rom_table.address += 1
    
    # second pass
    while parser_symbol_table.hasMoreCommands():
        parser_symbol_table.advance()
        
        # Determine the command type
        command_type = parser_symbol_table.commandType()
        
        if command_type == "A_COMMAND":
            symbol = parser.symbol()
            if ram_table.contains(symbol) is False:
                ram_table.addEntry(symbol, ram_table.address)
                ram_table.address += 1
                
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
            # @address
            if symbol.isdecimal():
                symbol_to_decimal = symbol
            # @variable/label
            elif symbol in ram_table:
                symbol_to_decimal = ram_table.map[symbol]
            elif symbol in rom_table:
                symbol_to_decimal = rom_table.map[symbol]
            binary_code = "0" + bin(int(symbol_to_decimal))[2:].zfill(15) + "\n"
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
    Assember("/Users/yan/Desktop/nand2teris/projects/06/pong/PongL.asm", "Pong.hack")
    Assember("/Users/yan/Desktop/nand2teris/projects/06/rect/RectL.asm", "Rect.hack")
    
if __name__ == "__main__":
    main()