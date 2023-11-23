import re
class Function:
    def __init__(self):
        self.Func_name = []
        self.Func_lines = []
        self.Parameter = []
    # Main
    def Declaration(self, name, parameter, lines, line):
        # Set Function name
        self.Func_name.append(name)
        # Set Function parameter
        parameter = parameter.split(',')
        self.Parameter.append(parameter)
        # Set Function blok statement
        Blok_Func = [] 
        for i in range(line, len(lines)):
            if 'fungsi' in lines[i]:
                continue
            elif '{' in lines[i]:
                continue
            elif '}' in lines[i]:
                self.Func_lines.append(Blok_Func)
                break
            else:
                Blok_Func.append(lines[i])
        # Jump to the next line
        line = i
        return line
    def Call(self, name, parameter, return_to, variable=[], in_variable=[]):
        set = []
        parameter = parameter.split(',')
        # Fix parameter
        for i in range(len(self.Func_name)):
            if self.Func_name[i] == name:
                for j in range(len(self.Parameter[i])):
                    if self.Parameter[i][j] not in variable:
                        self.Parameter[i][j] = ''
                while '' in self.Parameter[i]:
                    self.Parameter[i].remove('')
        # Set value of parameter
        for i in range(len(parameter)):
            for j in range(len(variable)):
                if parameter[i] == variable[j]:
                    parameter[i] = in_variable[j]
                    break
        # set return value
        for i in range(len(self.Func_name)):
            if self.Func_name[i] == name:
                set.append(self.Func_lines[i])
                set.append(self.Parameter[i])
                set.append(parameter)
                set.append(return_to)
        # self.Local_variable=[]
        return set
    def Return(self, set, variable, in_variable):
        for i in range(len(variable)):
            if variable[i] == set[0]:
                in_variable[i] = float(set[1])