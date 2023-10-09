class Basic:
    def __init__(self):
        self.File = open("Code.txt", "r")
        self.Variabel = []
        self.In_variabel = []
    def Check_line(self, scan):
        # print(scan)
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
        split = scan.split('=')
        self.Variabel.append(split[0])
        # if split[1].isdigit():

    # def Input(self): 
    def Output(self, scan): 
        print('This is print')
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
        self.File.close()

a = Basic()
a.Execution()