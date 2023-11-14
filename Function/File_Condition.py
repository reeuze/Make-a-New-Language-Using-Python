import re
from .Logical_operation import Class_Condition
class Condition:
    # Main
    def Main(self, type, cons, var=[], in_var=[], lines=[], line=0):
        key_word = r'==|!=|>=|<=|<|>|in|not in|and|or|\w+|\d+|\(|\)'
        result = [False,'','']  # Value cons, read begin, read end
        if cons is True: # 'Else:'
            result[0] = True
        else:
            cons = re.findall(key_word, cons)
            for i in range(len(cons)):
                for j in range(len(var)):
                    if cons[i] == var[j]:
                        cons[i] = in_var[j]
            operation = Class_Condition(cons)
            result[0] = operation.Main()
        
    # Sub Main
    def If_stm(self):
        print('A')
    def Elif_stm(self):
        print('B')
    def Else_stm(self):
        print('C')
    # Helper