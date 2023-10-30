from Support_file import Operation
class Main:
    def __init__(self):
        self.Name_file = "Code.txt"
        self.lines = []
        self.File = open(self.Name_file, "r")
    def Print(self):
        print("variabel : ", x.variable)
        print("value variabel : ", x.in_variable)
    def Check_line(self, scan):
        if '=' in scan:         # Inisialitation
            return 1
        elif 'input' in scan:   # Input
            return 2
        elif 'print' in scan:   # Output
            return 3
        elif (':' in scan) or ('goto' in scan):     # Label
            return 4
        elif ('if' in scan) or ('elif' in scan) or ('else' in scan):    # Condition
            return 5
        elif ('for' in scan):   # Looping
            return 6
        else:                   # Syntax Error
            return
    def Execution(self):
        with open(self.Name_file, 'r') as file:
            self.lines = file.readlines()
            line = 1
            while self.lines:
                s = self.Check_line(self.lines[line])
                # ============ #
                if s == 1:
                    x.Inisialitation(self.lines[line])
                elif s == 2:
                    x.Input(self.lines[line])
                elif s == 3:
                    x.Output(self.lines[line])
                elif s == 4:
                    set_line = x.Label(self.lines[line], self.lines, line)
                    if set_line != -1:
                        line = set_line
                # ============ #
                line += 1
    # def Execution(self):
    #     self.scan = self.File.readline().strip()
    #     line = 0
    #     while self.scan:
    #         s = self.Check_line(self.scan)
    #         # ============ #
    #         if s == 1:
    #             x.Inisialitation(self.scan)
    #         elif s == 2:
    #             x.Input(self.scan)
    #         elif s == 3:
    #             x.Output(self.scan)
    #         elif s == 4:
    #             x.Label(self.scan, self.Name_file, line)
    #         # ============ #
    #         self.scan = self.File.readline().strip()
    #         # self.Print()
    #         line += 1
    #     self.File.close()

a = Main()
x = Operation()
a.Execution()