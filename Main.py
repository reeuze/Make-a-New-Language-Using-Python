class Basic:
    def __init__(self):
        self.File = open("Code.txt", "r")
        self.Scan = ""
        self.Read = []
    def Inisialitation(self, scan, file):
        if scan in file:
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
        self.Scan = self.File.readline().strip()
        while self.Scan:
            # Check line

            self.Scan = self.File.readline().strip()
        self.File.close()

a = Basic()
a.Execution()