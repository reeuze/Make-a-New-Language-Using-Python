class Arithmetic_class:
    def __init__(self):
        self.Arithmetic = r'[\+\-\*\/\%\*\*]'
    def Integer_cal(self, input=[], index=0):
        self.Char = []
        self.Num = []
        while input:
            if input[index]==')':
                break
            elif input[index].isdigit():
                self.Num.append(str(input.pop(index)))
            elif self.Is_Operator(input[index]) is True:
                self.Char.append(input.pop(index))
            else:
                self.Num.append(str(input.pop(index)))
        while True:
            i = 0
            best  = 0
            for j, operator in enumerate(self.Char):
                if (operator=='+' or operator=='-') and best < 1:
                    n = 1
                    i = j
                elif (operator=='*' or operator=='/') and best < 2:
                    n = 2
                    i = j
                elif operator=='^' and best < 3:
                    n = 3
                    i = j
                best = n
            hasil = self.Operation(self.Num[i], self.Num[i+1], self.Char.pop(i))
            self.Num.insert(i, str(hasil))
            self.Num.pop(i+1)
            self.Num.pop(i+1)
            if len(self.Num) == 1:
                break
        input[index] = self.Num.pop()
        input[index-1] =  input.pop(index)
    # Helper
    def Operation(self, var1, var2, operator):
        if operator=='+':
            return var1+var2
        elif operator=='-':
            return var1-var2
        elif operator=='*':
            return var1*var2
        elif operator=='/':
            return var1/var2
        elif operator=='^':
            return var1**var2