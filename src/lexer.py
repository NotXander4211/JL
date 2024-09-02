import constants

class Lexer:
    def __init__(self, toLex):
        self.toLex = toLex
        self.index = 0
        self.lexed = []
        self.main = self.toLex.replace(" ", "")
        self.curChar = self.main[self.index]
        self.hasInput = True
    def checkInput(self):
        if self.main != "" and self.curChar != "":
            self.hasInput = True
            return
        self.hasInput = False
    def addT(TT, Value = None):
        TT = TT.lower()
        
    def advance(self):
        #possible outofbounds err, this should only be called if we have input still or maybe make it be ablt to retuen None(EOF)
        self.index =+ 1
        self.curChar = self.main[self.index]
         
    def getInt(self):
        pass
    def getStr(self):
        pass
    def Run(self):
        while self.hasInput:
            self.checkInput()
            if self.curChar in constants.DIGITS:
                self.addT(self.getInt())
