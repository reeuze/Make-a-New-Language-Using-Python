import re
from Support_file import Operation
class Main:
    def __init__(self, file):
        self.Name_file = file
        self.lines = []
    def Check_line(self, scan):
        # if ('untuk' in scan) or ('selama' in scan) and (':' in scan): # Looping
        #     return 6
        if ('=' and '[' and ']') in scan: # List
            return 7
        elif 'cetak' in scan: # Output
            return 3
        elif 'masukkan' in scan: # Input
            return 2
        elif ('jika' in scan) or ('jika_tidak' in scan) or ('lainnya' in scan) and (':' in scan): # Condition
            return 5
        elif '=' in scan: # Inisialitation
            return 1
        elif ('fungsi' in scan and '(' in scan and ')' in scan) or ('(' in scan and ')' in scan): # Function
            return 8
        elif 'kembalikan_nilai' in scan: # return value of function
            return 9
        elif (':' in scan) or ('ke' in scan): # Label
            return 4
    def Read_line(self, lines=[], line=0, line_end=0, nested=0, obj=Operation(), return_to=''):
        while 0 <= line < line_end:
            # remove space in begining
            if nested > 0:
                scan = lines[line].lstrip()
            else:
                scan = lines[line]
            s = self.Check_line(scan)
            # ============ #
            if s == 1:
                # print("detect inisialitation")
                obj.Inisialitation(scan)
            elif s == 2:
                # print("detect input")
                obj.Input(scan)
            elif s == 3:
                # print("detect output")
                obj.Output(scan)
            elif s == 4:
                # print("detect label")
                set_label = obj.Label(scan, lines, line)
                if set_label[0] != -1:
                    line = set_label[0]
                nested = set_label[1]
            elif s == 5:
                # print("detect condition")
                set_condition = [] # line, line_end, next_read_line
                set_condition = obj.Condition(lines, line, nested)
                self.Read_line(lines, set_condition[0], set_condition[1]+1, nested+1)
                line = set_condition[2]
            # elif s == 6 :
            #     # print("detect looping")
            #     set_loop = [[],[]]   # [lines], [line, end_line], next_read_line
            #     while True:
            #         set_loop = obj.Looping(lines[line], lines, line, nested)
            #         self.Read_line(set_loop[0], set_loop[1][0], set_loop[1][1]+1, nested+1)
            #         line = int(set_loop[2])
            elif s == 7:
                # print("detect list")
                obj.List(scan)
            elif s == 8:
                # print("detect function")
                set_function = obj.Function(scan, lines, line)
                if type(set_function) is int:
                    line = set_function
                elif set_function[3] is not None:
                    # print('detect func with return')
                    new_obj = Operation(set_function[1], set_function[2])
                    set_function = self.Read_line(set_function[0], 0, len(set_function[0]), nested+1, new_obj, set_function[3])
                    obj.Return(set_function, 'Get')
                else:
                    # print('detect func without return')
                    new_obj = Operation(set_function[1], set_function[2])
                    self.Read_line(set_function[0], 0, len(set_function[0]), nested+1, new_obj)
            elif s == 9:
                # print('detect return')
                set_return = []
                set_return.append(return_to)
                set_return.append(lines[line].replace('kembalikan_nilai ',''))
                obj.Return(set_return, 'Set')
                return set_return
            line += 1
    def Execution(self):
        with open(self.Name_file, 'r') as file:
            self.lines = file.readlines()
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].replace('\n', '')
            self.Read_line(self.lines, 0, len(self.lines), 0)

file = input('Execute : ')
a = Main(file)
a.Execution()