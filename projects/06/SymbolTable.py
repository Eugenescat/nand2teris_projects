
class SymbolTable:
    '''
    keeps a correspondence between symbolic labels and numeric addresses.
    '''
    
    def __init__(self) -> None:
        self.map = {}
        self.address = 0
        
    def addEntry(self, symbol, address) -> None:
        self.map.update({symbol: address})
        
    def contains(self, symbol) -> bool:
        return symbol in self.map
    
    def GetAddress(self, symbol) -> int:
        return self.map[symbol]