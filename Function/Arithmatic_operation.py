import re
class Class_Operation:
    def __init__(self, operation):
        self.Input = []
        self.Convert(operation)
    # Helper
    def Convert(self, input):
        self.Input.append('(')
        for char in input:
            self.Input.append(char)
        self.Input.append(')')
    def Is_Operator(self, character):
        operators = "+-*/^%"
        if character in operators:
            return True
    # Calculation
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
        elif operator=='%':
            return float(var1)%float(var2)
    def Calculation(self, input=[], index=0):
        self.Char = []
        self.Num = []
        while input:
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(str(input.pop(index)))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            else:
                self.Num.append(str(input.pop(index)))
        while True:
            i = 0
            best  = 0
            for j, operator in enumerate(self.Char):
                if (operator=='+' or operator=='-') and best < 1:
                    n = 1
                    i = j
                elif (operator=='*' or operator=='/' or operator=='%') and best < 2:
                    n = 2
                    i = j
                elif operator=='^' and best < 3:
                    n = 3
                    i = j
                best = n
            hasil = self.Operation(self.Num.pop(i), self.Num.pop(i), self.Char.pop(i))
            self.Num.insert(i, str(hasil))
            if len(self.Num) == 1:
                break
        input[index] = self.Num.pop()
        input[index-1] = input.pop(index)
    # Main
    def Main_Algorithm(self, input=[], index=0):
        input = self.Input
        for i in range(index, len(input)):
            if len(input) == 1:
                break
            elif input[i]=='(':
                self.Main_Algorithm(input, i+1)
            elif input[i]==')':
                self.Calculation(input, index)
                return
        return ''.join(self.Input)