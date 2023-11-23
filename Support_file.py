import re
from Function import File_Inisialitation, File_Output, File_Input, File_Label, File_Condition, File_Looping, File_List, File_Function

inisial = File_Inisialitation.Inisialitation()
output = File_Output.Output()
input = File_Input.Input()
label = File_Label.Label()
condition = File_Condition.Condition()
looping = File_Looping.Looping()
list = File_List.List()
func = File_Function.Function()
class Operation:
    def __init__(self, variable=[], in_variable=[]):
        self.variable = variable
        self.in_variable = in_variable
    # ===== Main Function =====
    def Inisialitation(self, scan):
        split = scan.split('=')
        if inisial.Input(split[0], split[1], self.variable, self.in_variable) is True:
            return
        elif inisial.Operation(split[0], split[1], self.variable, self.in_variable) is True:
            return
        elif inisial.Refill(split[0], split[1], self.variable, self.in_variable) is True:
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
    def Looping(self, scan, lines, line, nested):
        if 'untuk' in scan:
            looping.For(scan, lines, line, nested)
        elif 'selama' in scan:
            looping.While(scan, lines, line, nested)
    def List(self, scan):
        scan = scan.split('=')
        if list.Refill_elemen(scan[0], scan[1], self.variable, self.in_variable) is True:
            return
        elif list.Get_value(scan[0], scan[1], self.variable, self.in_variable) is True:
            return
        elif list.Input_list(scan[0], scan[1], self.variable, self.in_variable) is True:
            return
    def Function(self, scan, lines, line):
        if 'fungsi' in scan:
            # Declare
            scan = scan.replace('fungsi ', '')
            scan = scan.replace(')','')
            scan = scan.split('(')
            return func.Declaration(scan[0], scan[1], lines, line)
        elif '=' in scan:
            # Call with return
            scan = scan.split('=')
            scan[1] = scan[1].replace(')','')
            scan[1] = scan[1].split('(')
            print(scan)
            set = func.Call(scan[1][0], scan[1][1], scan[0], self.variable, self.in_variable)
            return set
        else:
            # Call without return
            scan = scan.replace(')','')
            scan = scan.split('(')
            set = func.Call(scan[0], scan[1], None, self.variable, self.in_variable)
            return set
    def Return(self, set, mode):
        if mode == 'Set':
            for i in range(len(self.variable)):
                if self.variable[i] == set[1]:
                    set[1] = self.in_variable[i]
        elif mode == 'Get':
            func.Return(set, self.variable, self.in_variable)
    def Syntax_error(self):
        print('syntax error!!')
    # ===== Helper =====