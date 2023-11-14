import re
class Condition:
    # Main
    def __init__(self):
        self.Input = []
    def Main(self, Input=[], index=0):
        Input = self.Input
        for i in range(len(Input)):
            if len(Input) == 1:
                break
            elif Input[i] == '(':
                self.Main(Input, i+1)
            elif Input[i] == ')':
                self.Calculation(Input, index)
                return
    # Sub Main
    def Calculation(sslf, Input=[], index=0):
        
    # Helper
    def Convert(self, scan):
        scan = '(' + scan + ')'
        key_word = r'==|!=|>=|<=|<|>|in|not in|and|or|not|\w+|\d+|\(|\)'
        self.Input = re.findall(key_word, scan)
    def Priority(self, operator):
        if '==' in operator:
            return 1
        elif '!=' in operator:
            return 2
        if ('>' or '<' or '>=' or '<=') in operator:
            return 3
        elif ('in' or 'not in') in operator:
            return 4
        elif ('and' or 'or' or 'not') in operator:
            return 5