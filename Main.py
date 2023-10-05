class Basic:
    def __init__(self):
        self.File = open("Code.txt", "r")
        self.Scan = ""
        self.Read = []
    def Open_file(self):
        self.File = open("Code.txt", "r")
    # def Inisialitation(self, scan):

    def Execution(self):
        while True:
            self.Scan = self.File.readline()
        self.File.close()

a = Basic()
a.Execution()