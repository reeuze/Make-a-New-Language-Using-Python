from Support_file import Operation
class Main:
    def __init__(self):
        self.Name_file = "Code.txt"
        self.lines = []
    def Print(self):
        print("variabel : ", x.variable)
        print("value variabel : ", x.in_variable)
    def Check_line(self, scan):
        if '=' in scan:         # Inisialitation
            return 1
        elif 'masukkan' in scan:   # Input
            return 2
        elif 'cetak' in scan:   # Output
            return 3
        elif (':' in scan) or ('ke' in scan):   # Label
            return 4
        elif (('jika' in scan) or ('jika tidak' in scan) or ('lainnya' in scan)) and (':' in scan):# Condition
            return 5
        elif ('for' in scan):   # Looping
            return 6
        elif ('=' and '[' and ']') in scan:     # List
            return 7
        elif 'def' in scan:     # Function
            return 8
        else:                   # Syntax Error
            return
    def Read_line(self, line=0, line_end=0):
        while 0 <= line < line_end:
            s = self.Check_line(self.lines[line])
            # ============ #
            if s == 1:
                # print("detect inisialitation")
                x.Inisialitation(self.lines[line])
            elif s == 2:
                # print("detect input")
                x.Input(self.lines[line])
            elif s == 3:
                # print("detect output")
                x.Output(self.lines[line])
            elif s == 4:
                # print("detect label")
                set_line = x.Label(self.lines[line], self.lines, line)
                if set_line != -1:
                    line = set_line
            elif s == 5:
                # print("detect condition")
                Decision = x.Condition(self.lines[line], self.lines, line)
                if Decision[0] is True:
                    self.Read_line(Decision[1], Decision[2])
            # ============ #
            # self.Print()
            line += 1
    def Execution(self):
        with open(self.Name_file, 'r') as file:
            self.lines = file.readlines()
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].replace('\n', '')
            self.Read_line(0, len(self.lines))
a = Main()
x = Operation()
a.Execution()