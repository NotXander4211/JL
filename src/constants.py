class Error:
    def __init__(self, name, details):
        self.name = name
        self.details = details
    def toString(self):
        return f"{self.name}: {self.details}"
    
class IllegalCharError(Error):
    def __init__(self, details):
        super.__init__(self, "IllegalCharError", details)

#TOKEN
class Token:
    def __init__(self, _type, val):
        self.type = _type
        self.value = val
    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}:&NOVALUE&"
    
#constant types
TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_EOF = "EOF"
TT_RBRACKET = "RBRACKET"
TT_LBRACKET = "LBRACKET"
TT_DQUOTE = "DQUOTE"
TT_SQUOTE = "SQUOTE"

#constants 
DIGITS = "0123456789"
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>:-_=!@#$%^&*()[].,?/"