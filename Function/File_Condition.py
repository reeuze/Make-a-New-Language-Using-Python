class Condition:
    # Main
    def __init__(self):
        self.Input = []
    def Main(self, scan):
        s = self.Check_type(scan)
        if s == 1/2/3/4/5/6:
            self.Comparison(scan)
        if s == 11/12/13:
            self.Logic()
        if s == 21/22:
            self.Member()
    # Condition Type
    # def If(self):
    #     print("A")
    # def If_else(self):
    #     print("B")
    # def If_else_if(self):
    #     print('C')
    # def Nested_if(self):
    #     print('D')
    def Check_type(self, scan):
        # Comparison
        if '==' in scan:
            return 1
        elif '!=' in scan:
            return 2
        elif '>' in scan:
            return 3
        elif '<' in scan:
            return 4
        elif '>=' in scan:
            return 5
        elif '<=' in scan:
            return 6
        # Member
        elif 'in' in scan:
            return 21
        elif 'not in' in scan:
            return 22
        # Logic
        elif 'and' in scan:
            return 11
        elif 'or' in scan:
            return 12
        elif 'not' in scan:
            return 13
    # Helper
    def Comparison(self, input):
        print('E')
    def Logic(self):
        print('F')
    def Member(self):
        print('H')