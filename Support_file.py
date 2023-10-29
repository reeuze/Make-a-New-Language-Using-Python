from Function import File_Inisialitation, File_Output

inisial = File_Inisialitation.Inisialitation()
output = File_Output.Output()
class Operation:
    def __init__(self):
        self.variable = []
        self.in_variable = []
    def Inisialitation(self, scan):
        split = scan.split('=')
        if inisial.Refill(split[0], split[1], self.variable, self.in_variable) is True:
            return
        elif inisial.Input(split[0], split[1], self.variable, self.in_variable) is True:
            return
    def Input(self):
        print("A")
    def Output(self, scan):
        scan = output.Get_output(scan)
        output.Main(scan, self.variable, self.in_variable)
    # def Label(self, scan):
    # def Condition(self): 
    # def Looping(self): 
    # def Stack(self): 
    # def Function(self): 
    def Syntax_error(self):
        print('syntax error!!')