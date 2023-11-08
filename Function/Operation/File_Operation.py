import re
class Operation:
    def __init__(self):
        self.Input = []
        self.Operator = r'([\+\-\*\/\%\*\*]|==|!=|>=?|<=?|and|or|not|[\+\-\*\*\/%]?=|\w+|\d+|\(|\))'
        self.Arithmetic = r'[\+\-\*\/\%\*\*]'
        self.Comparison = r'==|!=|>=?|<=?'
        self.Logic = r'and|or|not'
        self.Task = r'[\+\-\*\*\/%]?='
        # self.Bitwise = r'&|\||\^|~|<<|>>'
        # self.Member = r'in|not in'
        # self.Identity = r'is|is not'
    # Helper
    def Convert(self, input):
        input = '(' + input + ')'
        self.Input = re.findall(self.Operator, input)
        for i, char in enumerate(self.Input):
            if char.isdigit():
                self.Input[i] = int(char)
    # def Take_list(self, input=[], i):
    #     for j in range(len(input)):

    # def Check_type(self, input=[]):
        
    def Algorithm(self, input=[], index=0):
        for i in range(index, len(input)):
            if len(input) == 1:
                break
            elif input[i]=='(':
                self.Algorithm(input, i+1)
            elif input[i]==')':
                # list = 
                # check logic

                return
        return ''.join(self.Input)

# input = "(A==B) and (A>=12)"
# a = Operation()
# a.Convert(input)
# print(a.Input)