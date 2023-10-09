class Basic:
    def __init__(self):
        self.File = open("Code.txt", "r")
        self.Variabel = []
    def Check_line(self, scan):
        # print(scan)
        if '=' in scan:
            return 1
        elif 'input' in scan:
            return 2
        elif 'print' in scan:
            return 3
        elif ('if' in scan) or ('elif' in scan) or ('else' in scan):
            return 4
        elif ('for' in scan):
            return 5
        else:
            print(99)
            return
    def Inisialitation(self, scan):
        print('This is inisialisation !!')
    # def Input(self): 
    def Output(self, scan): 
        print('This is print')
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