class Output:
    def __init__(self):
        self.output = ""
        self.string = []
    def Main(self, str, var=[], in_var=[]):
        self.string = str.split(',')
        for i in range(len(self.string)):
            if '"' in self.string[i]:
                self.Direct('"', self.string[i])
            elif "\'" in self.string[i]:
                self.Direct("\'", self.string[i])
            else:
                self.Variable(self.string[i], var, in_var)
        print(self.output)
        self.output = ""
        self.string = []
    # Output type
    def Direct(self, type, str):
        self.output += self.Get_string(type, str)
    def Variable(self, string, var=[], in_var=[]):
        for i in range(len(var)):
            if string==var[i]:
                self.output += str(in_var[i])
                break
    # Helper
    def Get_output(self, string):
        open = string.find('(') + 1
        close = string.find(')')
        return string[open:close]
    def Get_string(self, type, string):
        Text = []
        begin = 0
        while True:
            begin = string.find(type, begin)
            if begin == -1:
                break
            end = string.find(type, begin + 1)
            if end == -1:
                break
            Text.append(string[begin + 1:end])
            begin = end + 1
        return ''.join(Text)