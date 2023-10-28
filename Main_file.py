from Support_file import Operation
class Main:
    def __init__(self):
        self.File = open("Code.txt", "r")
    def Print(self):
        print("variabel : ", x.Variabel)
        print("value variabel : ", x.In_variabel)
    def Check_line(self, scan):
        if '=' in scan:
            return 1
        elif 'input' in scan:
            return 2
        elif 'print' in scan:
            return 3
        elif ':' in scan:
            return 4
        elif ('if' in scan) or ('elif' in scan) or ('else' in scan):
            return 5
        elif ('for' in scan):
            return 6
        else:
            return
    def Inisialitation(self, scan):
        print("inisialitation detected !")
        split = scan.split('=')
        x.Variabel.append(split[0])
        if split[1].isdigit():
            x.In_variabel.append(split[1])
        else:
            x.In_variabel.append(None)
    # def Input(self): 
    def Output(self, scan):
        print("print detected !") 
        scan = x.Get_string(scan)
        if '"' in scan:
            print("detect string")
            scan = x.Get_string(scan)
            print(scan)
        elif "\'" in scan:
            print("detect string")
            scan = x.Get_string(scan)
            print(scan)
        else:
            print("detect var")
            print(x.In_variabel[x.Check_var(scan)])
    # def Label(self, scan):
    # def Condition(self): 
    # def Looping(self): 
    # def Stack(self): 
    # def Function(self): 
    def Syntax_error(self):
        print('syntax error!!')
    def Execution(self):
        self.scan = self.File.readline().strip()
        while self.scan:
            self.temp = []
            # Check Function
            s = self.Check_line(self.scan)
            if s == 1:
                self.Inisialitation(self.scan)
            elif s == 3:
                self.Output(self.scan)
            # ============ #
            self.scan = self.File.readline().strip()
            self.Print()
        self.File.close()

a = Main()
x = Operation()
a.Execution()