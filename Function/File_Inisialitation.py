class Inisialitation:
    # Inisial Type
    def Refill(self, var, in_var, variable=[], in_variable=[]):
        for i in range(len(variable)):
            if var == variable[i]:
                in_variable[i] = in_var
                return True
        return False
    def Input(self, var, in_var, variable=[], in_variable=[]):
        if self.Is_Operator(in_var) is False:
            variable.append(var)
            in_variable.append(in_var)
            return True
        else:
            return False
    def Operation(self):
        print("C")
    # Helper
    def Is_Operator(self, character):
        operators = "+-*/^"
        if character in operators:
            return True
        else:
            return False