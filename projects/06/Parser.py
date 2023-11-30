
class Parser:
    '''
    Class: Parser
    Description: Asscess the input code. 
    Read an assembly language command, and provides convenient access to the command's components(fileds and symbols).
    Remove all white space and comments.
    '''
    
    def __init__(self, file_name) -> None:
        '''
        Opens the input file/stream and gets ready to parse it.
        '''
        self.all_instructions = self.strip_commands(file_name)
        # current index of commands
        self.cur = -1
        # currently parsing command
        self.instruction = ""
        
    def strip_commands(self, file_name) -> list:
        stripped_commands = []

        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # erase leading and tailing whitespace from the line
                line = line.strip()
                # erase the comments from the line
                line = line.split("//")[0].strip()
                # erase the rest whitespace
                line = line.replace(" ", "")
                # If the line is not empty, add it to the list of stripped commands
                if line != "":
                    stripped_commands.append(line)
                
        return stripped_commands
                
    def hasMoreCommands(self) -> bool:
        '''
        Are there more commands in the input?
        '''
        return (len(self.all_instructions) - self.cur) > 1
    
    def advance(self) -> None:
        '''
        Reads the next command from the input and makes it the current command. 
        Should be called only if hasMoreCommands ( ) is true.
        Initially there is no current command
        '''
        self.cur += 1
        self.instruction = self.all_instructions[self.cur]
            
    
    def commandType(self) -> str:
        '''
        Returns the type of the current command
        '''
        if self.instruction[0] == "@":
            return "A_COMMAND"
        elif self.instruction[0] == "(":
            return "L_COMMAND"
        else:
            return "C_COMMAND"
        
        
    def symbol(self) -> str:
        '''
        Returns the symbol or decimal Xxx of the current command @xxx or (xxx). 
        Should be called only when commandType( ) is A COMMAND OT L COMMAND.
        '''
        # e.g. @100 or @loop
        if self.commandType() == "A_COMMAND":
            return self.instruction[1:]
        # e.g. (loop)
        elif self.commandType() == "L_COMMAND":
            return self.instruction[1:-1]
    
    def dest(self) -> str:
        '''
        Returns the dest mnemonic in the current C-command (8 possibilities). 
        Should be called only when commandType() is C-COMMAND.
        e.g. dest=comp;jump
        e.g. dest=comp
        e.g. comp;jump
        '''
        if "=" in self.instruction:
            splitted_inst = self.instruction.split("=")
            dest_mnemonic = splitted_inst[0]
        else:
            dest_mnemonic = "null"
            
        return dest_mnemonic
        
    def comp(self) -> str:
        '''
        Returns the comp mnemonic in the current C-command (28 posibilities).
        Should be called only when commanType() is C_command
        '''
        if "=" in self.instruction:
            splitted_inst = self.instruction.split("=")
            if ";" in splitted_inst[1]:
                splitted_again_inst = splitted_inst[1].split(";")
                comp_mnemonic = splitted_again_inst[0]
            else:
                comp_mnemonic = splitted_inst[1]
        else:
            comp_mnemonic = self.instruction.split(";")[0]
        
        return comp_mnemonic
        
    def jump(self) -> str:
        '''
        Returns the jump mnemonic in the current C-command (8-possibilities).
        Should be called only when commandType() is C_command
        '''
        if ";" in self.instruction:
            splitted_inst = self.instruction.split(";")
            jump_mnemonic = splitted_inst[1]
        else:
            jump_mnemonic = "null"
        
        return jump_mnemonic
        
