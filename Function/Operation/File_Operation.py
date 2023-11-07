import re
class Operation:
    def __init__(self):
        self.Input = []
        # self.Character = []
        # self.Postfix = []
        self.Arithmetic = r'[\+\-\*\/\%\*\*]'
        self.Comparison = r'==|!=|>=?|<=?'
        self.Logic = r'and|or|not'
        self.Task = r'[\+\-\*\*\/%]?='
        # self.Bitwise = r'&|\||\^|~|<<|>>'
        # self.Member = r'in|not in'
        # self.Identity = r'is|is not'
    # Helper
    def Convert(self, input):
        self.Input.append('(')
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        self.Input = re.findall(self.Arithmetic, input)
        for char in input:
            self.Input.append(char)
        self.Input.append(')')
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
    def Check_type(self, operator=[]):
        Arithmetic = r'[\+\-\*\/\%\*\*]'
        Comparison = r'==|!=|>=?|<=?'
        Logic = r'and|or|not'
        Bitwise = r'&|\||\^|~|<<|>>'
        Task = r'[\+\-\*\*\/%]?='
        Member = r'in|not in'
        Identity = r'is|is not'

    # Type Operation
    def Operation(self, var1, var2, operator):
        if operator=='+':
            return var1+var2
        elif operator=='-':
            return var1-var2
        elif operator=='*':
            return var1*var2
        elif operator=='/':
            return var1/var2
        elif operator=='^':
            return var1**var2
    # def Fix_character(self, character=[], postfix=[]):
    #     i = len(character) - 1
    #     while i >= 0:
    #         if character[i]=='(':
    #             character.pop()
    #             break
    #         else:
    #             postfix.append(character.pop())
    #         i -= 1
    # Calculation in bracket
    def Integer_cal(self, input=[], index=0):
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
                elif (operator=='*' or operator=='/') and best < 2:
                    n = 2
                    i = j
                elif operator=='^' and best < 3:
                    n = 3
                    i = j
                best = n
            hasil = self.Operation(self.Num[i], self.Num[i+1], self.Char.pop(i))
            self.Num.insert(i, str(hasil))
            self.Num.pop(i+1)
            self.Num.pop(i+1)
            if len(self.Num) == 1:
                break
        input[index] = self.Num.pop()
        input[index-1] =  input.pop(index)
    # def String_cal(self)
    # def Logic_cal(self)
    # def Replace_operator(self, op1, op2):
    #     i = 0
    #     j = 0
    #     if op1=='+' or op1=='-':
    #         i = 1
    #     elif op1=='*' or op1=='/':
    #         i = 2
    #     elif op1=='^':
    #         i = 3
    #     if op2=='+' or op2=='-':
    #         j = 1
    #     elif op2=='*' or op2=='/':
    #         j = 2
    #     elif op2=='^':
    #         j = 3
    #     if i>=j:    # stack more important
    #         self.Postfix.append(op1)
    #         self.Character.pop()
    #         self.Character.append(op2)
    #     elif i<j:   # input more important
    #         self.Character.append(op2)
    def Algorithm(self, input=[], index=0):
        for i in range(index, len(input)):
            if len(input) == 1:
                break
            elif input[i]=='(':
                self.Algorithm(input, i+1)
            elif input[i]==')':
                self.Integer_cal(input, index)
                # check logic
                return
        return ''.join(self.Input)

input = "1 is one"
# input2 = "1+(2/3-(4*5^6)+7)*8"
a = Operation()
a.Convert(input)
print(a.Input)
# hasil = a.Algorithm(a.Input)
# print("\nHasilnya : ", hasil)