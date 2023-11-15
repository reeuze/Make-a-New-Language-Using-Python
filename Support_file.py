import re
from Function import File_Inisialitation, File_Output, File_Input, File_Label, File_Condition

inisial = File_Inisialitation.Inisialitation()
output = File_Output.Output()
input = File_Input.Input()
label = File_Label.Label()
condition = File_Condition.Condition()
class Operation:
    def __init__(self):
        self.variable = []
        self.in_variable = []
    # ===== Main Function =====
    def Inisialitation(self, scan):
        split = scan.split('=')
        if inisial.Refill(split[0], split[1], self.variable, self.in_variable) is True:
            return
        elif inisial.Input(split[0], split[1], self.variable, self.in_variable) is True:
            return
        elif inisial.Operation(split[0], split[1], self.variable, self.in_variable) is True:
            return
    def Input(self, scan):
        scan = input.Get_input(scan)
        scan = scan.split(',')
        # output.Main(scan[0], self.variable, self.in_variable)
        input.Main(scan, self.variable, self.in_variable)
    def Output(self, scan):
        scan = output.Get_output(scan)
        output.Main(scan, self.variable, self.in_variable)
    def Label(self, scan, lines, line):
        if label.Label_name(scan, line) is True:
            return -1
        else:
            return label.Goto_statement(scan, lines, line)
    def Condition(self, lines, line, nested):
        set_line = condition.Main(self.variable, self.in_variable, lines, line, nested)
        return set_line
    # def Looping(self): 
    # def Stack(self): 
    # def Function(self): 
    def Syntax_error(self):
        print('syntax error!!')
    # ===== Helper =====