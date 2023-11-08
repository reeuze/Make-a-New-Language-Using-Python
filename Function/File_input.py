class Input:
    # Main
    def Main(self):
        print('A')
    # Helper
    def Get_input(self, string):
        open = string.find('(') + 1
        close = string.find(')')
        return string[open:close]