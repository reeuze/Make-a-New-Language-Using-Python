from Support_file import Operation
class Main:
    def __init__(self):
        self.File = open("Code.txt", "r")
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
        elif ':' in scan:       # Label
            return 4
        elif ('if' in scan) or ('elif' in scan) or ('else' in scan):    # Condition
            return 5
        elif ('for' in scan):   # Looping
            return 6
        else:                   # Syntax Error
            return
    def Execution(self):
        self.scan = self.File.readline().strip()
        while self.scan:
            self.temp = []
            # Check Function
            s = self.Check_line(self.scan)
            if s == 1:
                x.Inisialitation(self.scan)
            elif s == 3:
                x.Output(self.scan)
            # ============ #
            self.scan = self.File.readline().strip()
            # self.Print()
        self.File.close()

a = Main()
x = Operation()
a.Execution()