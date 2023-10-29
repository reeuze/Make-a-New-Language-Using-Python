from Function import File_Inisialitation, File_Output

inisial = File_Inisialitation.Inisialitation()
output = File_Output.Output()
class Operation:
    def __init__(self):
        self.variable = []
        self.in_variable = []
    def Inisialitation(self, scan):
        print("inisialitation detected !")
        split = scan.split('=')
        self.variable.append(split[0])
        if split[1].isdigit():
            self.in_variable.append(split[1])
        else:
            self.in_variable.append(None)
    def Input(self):
        print("A")
    def Output(self, scan):
        print("print detected !") 
        scan = output.Get_output(scan)
        output.Main(scan, self.variable, self.in_variable)
    # def Label(self, scan):
    # def Condition(self): 
    # def Looping(self): 
    # def Stack(self): 
    # def Function(self): 
    def Syntax_error(self):
        print('syntax error!!')