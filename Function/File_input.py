class Input:
    # Main
    def Main(self, scan, variable, in_variable):
        scan[0] = scan[0].replace('\'', '')
        if scan[1] in variable:
            i = variable.index(scan[1])
            Input = input(scan[0])
            in_variable[i] = Input
        else:
            variable.append(scan[1])
            Input = input(scan[0])
            in_variable.append(Input)
    # Helper
    def Get_input(self, string):
        open = string.find('(') + 1
        close = string.find(')')
        return string[open:close]