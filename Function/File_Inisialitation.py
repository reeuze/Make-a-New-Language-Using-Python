import re
from .Arithmatic_operation import Class_Operation
class Inisialitation:
    # Inisial Type
    def Refill(self, var, in_var, variable=[], in_variable=[]):
        for i in range(len(variable)):
            if var == variable[i]:
                in_variable[i] = in_var
                return True
        return False
    def Input(self, var, in_var, variable=[], in_variable=[]):
        if self.Is_Operator(in_var) is False:
            variable.append(var)
            in_variable.append(in_var)
            return True
        else:
            return False
    def Operation(self, var, in_var, variable=[], in_variable=[]):
        Token = r'[\+\-\*\/\%\*\*\^]|\w+|\d+|\(|\)'
        Stack_var =  re.findall(Token, in_var)
        for i in range(len(Stack_var)):
            for j in range(len(variable)):
                if Stack_var[i] == variable[j]:
                    Stack_var[i] = in_variable[j]
        operation = Class_Operation(Stack_var)
        result = operation.Main_Algorithm()
        if self.Refill(var, result, variable, in_variable) is True:
            return True
        else:
            variable.append(var)
            in_variable.append(result)
            return True
    # Helper
    def Is_Operator(self, in_var):
        operators = "+-*/^"
        Token = r'[\+\-\*\/\%\*\*\^]|\w+|\d+|\(|\)'
        Stack_var = re.findall(Token, in_var)
        for i in range(len(Stack_var)):
            if Stack_var[i] in operators:
                return True
        return False