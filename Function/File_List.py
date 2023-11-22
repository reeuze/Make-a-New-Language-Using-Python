class List:
    def __init__(self):
        self.list = []
    # Main
    # Set value
    def Input_list(self, var, in_var, variable=[], in_variable=[]):
        print(var, in_var)
        variable.append(var)
        in_var = in_var.replace(']', '')
        in_var = in_var.replace('[', '')
        in_var = in_var.split(',')
        in_variable.append(in_var)
        return True
    def Refill_list(self, var, in_var, variable=[], in_variable=[]):
        print('B')
    def Input_elemen(self, var, in_var, variable=[], in_variable=[]):
        print('C')
    def Refill_elemen(self, var, in_var, variable=[], in_variable=[]):
        if ('[' and ']') in var:
            var = var.replace(']', '')
            var = var.split('[')
            if in_var.isdigit():
                for i in range(len(variable)):
                    if variable[i] == var[0]:
                        in_variable[i][int(var[1])] = in_var
            elif type(in_var) is str:
                for i in range(len(variable)):
                    if in_var == variable[i]:
                        in_var = in_variable[i]
                for i in range(len(variable)):
                    if variable[i] == var[0]:
                        in_variable[i][int(var[1])] = in_var
            return True
        else:
            return False
    # Take value
    def Get_value(self, var, in_var, variable=[], in_variable=[]):
        if ('[' and ']') in in_var:
            in_var = in_var.replace(']', '')
            in_var = in_var.split('[')
            if in_var[0] == '':
                return False
            for i in range(len(variable)):
                if variable[i] == in_var[0]:
                    in_var = in_variable[i][int(in_var[1])]
            for i in range(len(variable)):
                if variable[i] == var:
                    in_variable[i] = in_var
            return True
        else:
            return False