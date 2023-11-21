from .File_Inisialitation import Inisialitation
# from .Arithmatic_operation import Class_Operation
from .Logical_operation import Class_Condition
inisial = Inisialitation()
# Arithmetic = Class_Operation()
class Looping:
    def __init__(self):
        self.Loop_lines = []
    # Main
    def For(self, scan, lines, line, nested):
        # Calculate how many times the looping occurs
        # Take and split the condition
        scan = scan.split()
        scan[1] = scan[1].replace(':','')
        scan[1] = scan[1].replace('(','')
        scan[1] = scan[1].replace(')','')
        scan = scan[1].split(';')
        print(scan)
        # Take inisial
        split = scan[0].split('=')
        while True:
            if inisial.Input(split[0], split[1], self.variable, self.in_variable) is True:
                break
            elif inisial.Operation(split[0], split[1], self.variable, self.in_variable) is True:
                break
            elif inisial.Refill(split[0], split[1], self.variable, self.in_variable) is True:
                break
        var = split[0]
        # Take Logic
        if '<=' in scan[1]:
            print('A')
        elif '<' in scan[1]:
            print('B')
        # looping > 0
        # Insert looping statement blocks into the loop_lines stack as many times as looping occurs



        # looping < 0
        print('A')
    def While(self, scan, lines, line, nested):
        print('A')
    # Helper
    def Check_type(self):
        print('A')