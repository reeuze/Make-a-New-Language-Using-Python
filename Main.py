class Basic:
    def __init__(self):
        self.File = open("Code.txt", "r")
        self.Variabel = []
    def Inisialitation(self, scan):
        if '=' in scan:
            return True
        else:
            return False
    # def Input(self): 
    # def Output(self): 
    # def Condition(self): 
    # def Looping(self): 
    # def Stack(self): 
    # def Function(self): 
    def Execution(self):
        self.scan = self.File.readline().strip()
        while self.scan:
            self.temp = []
            # Check Function
            if self.Inisialitation(self.scan) is True:
                continue

            self.scan = self.File.readline().strip()
        self.File.close()

a = Basic()
a.Execution()