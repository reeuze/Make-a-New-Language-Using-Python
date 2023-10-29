class Output:
    def Main(self, str, var=[], in_var=[]):
        self.output = ""
        self.string = []
        self.string = str.split(',')
        for i in range(len(self.string)):
            if '"' in self.string[i]:
                print("detect string")
                self.output += self.Get_string('"', self.string[i])
            elif "\'" in self.string[i]:
                print("detect string")
                self.output += self.Get_string("\'", self.string[i])
            else:
                print("detect var")
    def String(self, string):
        print("A")
    def Variable(self):
        print("B")
    # Helper
    def Get_output(self, string):
        open = string.find('(') + 1
        close = string.find(')')
        return string[open:close]
    def Get_string(self, type, string):
        Teks = []
        begin = 0
        while True:
            begin = string.find(type, begin)
            if begin == -1:
                break
            end = string.find(type, begin + 1)
            if end == -1:
                break
            Teks.append(string[begin + 1:end])
            begin = end + 1
        return Teks