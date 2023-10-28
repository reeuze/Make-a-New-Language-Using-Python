import re
class Operation:
    def __init__(self):
        self.Variabel = []
        self.In_variabel = []
    def Get_string(self, string):
        hasil = re.findall(r"\((.*?)\)", string)
        print(hasil)
        return hasil
    # def Get_string(self, string, begin, end):
    #     open = string.find(begin) + 1
    #     close = string.find(end)
    #     return string[open:close]
    def Check_var(self, variable):
        print(variable)
        for i in range(len(self.Variabel)):
            if variable == self.Variabel[i]:
                print(i)
                return i
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True