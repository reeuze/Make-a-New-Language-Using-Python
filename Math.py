class Operation:
    def __init__(self):
        self.Variabel = []
        self.In_variabel = []
    def Operation(self, var1, var2, operator):
        if operator=='+':
            return float(var1)+float(var2)
        elif operator=='-':
            return float(var1)-float(var2)
        elif operator=='*':
            return float(var1)*float(var2)
        elif operator=='/':
            return float(var1)/float(var2)
        elif operator=='^':
            return float(var1)**float(var2)
    def Get_string(self, string):
        open = string.find('(') + 1
        close = string.find(')')
        return string[open:close]
    def Check_var(self, variable):
        for i in range(len(self.Variabel)):
            if variable == self.Variabel[i]:
                return i
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True