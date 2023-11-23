from Support_file import Operation
class Main:
    def __init__(self, file):
        self.Name_file = file
        self.lines = []
    # def Print(self):
    #     print("variabel : ", x.variable)
    #     print("value variabel : ", x.in_variable)
    def Check_line(self, scan):
        if ('untuk' in scan) or ('selama' in scan) and (':' in scan): # Looping
            return 6
        elif ('=' and '[' and ']') in scan: # List
            return 7
        elif '=' in scan: # Inisialitation
            return 1
        elif 'masukkan' in scan: # Input
            return 2
        elif 'cetak' in scan: # Output
            return 3
        elif ('jika' in scan) or ('jika_tidak' in scan) or ('lainnya' in scan) and (':' in scan): # Condition
            return 5
        elif (':' in scan) or ('ke' in scan): # Label
            return 4
        elif ('fungsi' in scan and '(' in scan and ')' in scan) or ('(' in scan and ')' in scan): # Function
            return 8
        elif 'kembalikan_nilai' in scan: # return value of function
            return 9
        else: # Syntax Error
            return 99
    def Read_line(self, lines=[], line=0, line_end=0, nested=0, obj=Operation(), return_to=''):
        while 0 <= line < line_end:
            s = self.Check_line(lines[line])
            # ============ #
            if s == 1:
                # print("detect inisialitation")
                obj.Inisialitation(lines[line])
            elif s == 2:
                # print("detect input")
                obj.Input(lines[line])
            elif s == 3:
                # print("detect output")
                obj.Output(lines[line])
            elif s == 4:
                # print("detect label")
                set_line = obj.Label(lines[line], lines, line)
                if set_line != -1:
                    line = set_line
            elif s == 5:
                # print("detect condition")
                set = [] # line, line_end, next_read_line
                set = obj.Condition(lines, line, nested)
                self.Read_line(lines, set[0], set[1]+1, nested+1)
                line = set[2]
                # print(self.lines[line])
            elif s == 6 :
                # print("detect looping")
                set_loop = [[],[]]   # [lines], [line, end_line], next_read_line
                while True:
                    set_loop = obj.Looping(lines[line], lines, line, nested)
                    self.Read_line(set_loop[0], set_loop[1][0], set_loop[1][1]+1, nested+1)
                    line = int(set_loop[2])
            elif s == 7:
                # print("detect list")
                obj.List(lines[line])
            elif s == 8:
                # print("detect function")
                set = obj.Function(lines[line], lines, line)
                if type(set) is int:
                    line = set
                elif set[3] is not None:
                    new_obj = Operation(set[1], set[2])
                    set = self.Read_line(set[0], 0, len(set[0]), nested+1, new_obj, set[3])
                    obj.Return(set, 'Get')
                else:
                    new_obj = Operation(set[1], set[2])
                    self.Read_line(set[0], 0, len(set[0]), nested+1, new_obj)
            if s == 9:
                # print('detect return')
                set = []
                set.append(return_to)
                set.append(lines[line].replace('kembalikan_nilai '))
                print(set)
                obj.Return(set, 'Set')
                return set
            # else:
            #     line += 1
            #     return
            # ============ #
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