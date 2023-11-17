import re
class Class_Condition:
    # Main
    def __init__(self, scan):
        self.input = []
        self.Convert(scan)
        self.input = scan
    def Main(self, Input=[], index=0):
        Input = self.input
        for i in range(index, len(Input)):
            if len(Input) == 1:
                break
            elif Input[i] == '(':
                self.Main(Input, i+1)
            elif Input[i] == ')':
                self.Calculation(Input, index)
                return
        return str(self.input)
    # Sub Main
    def Calculation(self, Input=[], index=0):
        operator = []
        value = []
        key_word = r'==|!=|>=|<=|<|>|in|not in|and|or'
        operan = re.findall(key_word, ''.join(Input))
        print(Input, index, Input[index])
        while Input:
            print(Input[index])
            if Input[index]==')':
                break
            elif Input[index] in operan:
                operator.append(Input.pop(index))
            else:
                value.append(Input.pop(index))
        print(operator, value)
        while len(value) != 1:
            i = self.Priority(operator)
            result = self.Compare(value.pop(i), value.pop(i), operator.pop(i))
            value.insert(i, str(result))
        Input[index] = value.pop()
        Input[index-1] = Input.pop(index)
    def Compare(self, var1, var2, operator):
        # Compare Nummber
        if operator == '==':
            if float(var1) == float(var2):
                return True
            else:
                return False
        elif operator == '!=':
            if float(var1) != float(var2):
                return True
            else:
                return False
        elif operator == '>=':
            if float(var1) >= float(var2):
                return True
            else:
                return False
        elif operator == '<=':
            if float(var1) <= float(var2):
                return True
            else:
                return False
        elif operator == '>':
            if float(var1) > float(var2):
                return True
            else:
                return False
        elif operator == '<':
            if float(var1) < float(var2):
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
        # scan = '(' + scan + ')'
        # key_word = r'\b(==|!=|>=|<=|<|>|in|not in|and|or|\d+\.\d+|d+|\(|\)|\w+)\b'
        # self.input = re.findall(key_word, scan)
        for i in range(len(self.input)):
            if self.input[i] == 'True':
                self.input[i] = True
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