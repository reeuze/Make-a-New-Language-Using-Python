import re
class Class_Condition:
    # Main
    def __init__(self, scan):
        self.input = []
        self.Convert(scan)
    def Main(self, Input=[], index=0):
        Input = self.input
        for i in range(len(Input)):
            if len(Input) == 1:
                break
            elif Input[i] == '(':
                self.Main(Input, i+1)
            elif Input[i] == ')':
                self.Calculation(Input, index)
                return
    # Sub Main
    def Calculation(self, Input=[], index=0):
        operator = []
        value = []
        operator = r'==|!=|>=|<=|<|>|in|not in|and|or'
        operator = re.findall(operator, ''.join(Input))
        while input:
            if input[index]==')':
                break
            elif input[index] in operator:
                operator.append(input.pop(index))
            else:
                value.append(input.pop(index))
        while len(input) != 1:
            i = self.Priority(operator)
            result = self.Compare(value.pop(i), value.pop(i), operator.pop(i))
            value.insert(i, str(result))
    def Compare(self, var1, var2, operator):
        # Compare Nummber
        if operator == '==':
            if int(var1) == int(var2):
                return True
            else:
                return False
        elif operator == '!=':
            if int(var1) != int(var2):
                return True
            else:
                return False
        elif operator == '>=':
            if int(var1) >= int(var2):
                return True
            else:
                return False
        elif operator == '<=':
            if int(var1) <= int(var2):
                return True
            else:
                return False
        elif operator == '>':
            if int(var1) > int(var2):
                return True
            else:
                return False
        elif operator == '<':
            if int(var1) < int(var2):
                return True
            else:
                return False
        # Member
        if operator == 'in':
            if (var1 in var2) is True:
                return True
            else:
                return False
        if operator == 'not in':
            if (var1 not in var2) is True:
                return True
            else:
                return False
        # Logic
        if operator == 'and':
            if (var1 and var2) is True:
                return True
            else:
                return False
        if operator == 'or':
            if (var1 or var2) is True:
                return True
            else:
                return False
    # Helper
    def Convert(self, scan):
        scan = '(' + scan + ')'
        key_word = r'==|!=|>=|<=|<|>|in|not in|and|or|\w+|\d+|\(|\)'
        self.input = re.findall(key_word, scan)
    def Priority(self, operator):
        value = 0
        best = 0
        index = 0
        for i in range(len(operator)):
            if '==' in operator:
                value = 1
            elif '!=' in operator:
                value = 2
            if ('>' or '<' or '>=' or '<=') in operator:
                value = 3
            elif ('in' or 'not in') in operator:
                value = 4
            elif ('and' or 'or' or 'not') in operator:
                value = 5
            if value > best:
                best = value
                index = i
        return index