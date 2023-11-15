import re
from .Logical_operation import Class_Condition
class Condition:
    # Main
    def Main(self, var=[], in_var=[], lines=[], line=0, nested=0):
        key_word = r'==|!=|>=|<=|<|>|in|not in|and|or|\w+|\d+|\(|\)'
        cons = []
        line_stm = []
        tmp = []
        i = line
        print(i)
        nest = 0
        blok = 0
        while i < len(lines):
            print(lines[i])
            nest = self.Nested(lines[i])
            print(nest)
            # Insert condition
            if ('jika' in lines[i]) and (blok == 0):
                # set condition
                con = lines[i].split()
                con[1] = con[1].replace(':', '')
                cons.append(con[1])
                blok += 1
                # add number begin line
                tmp.append(i+1)
            elif ('jika_tidak' in lines[i]) and (nest == nested):
                # add number last line
                tmp.append(i)
                line_stm.append(tmp)
                # set condition
                con = lines[i].split()
                con[1] = con[1].replace(':', '')
                cons.append(con[1])
                # add number begin line
                tmp.append(i+1)
            elif ('lainnya' in lines[i]) and (nest == nested):
                # add number last line
                tmp.append(i)
                line_stm.append(tmp)
                # set value 'else'
                cons.append(True)
                tmp.append(i+1)
            # Masukkan blok statementnya
            elif nest > nested:
                i += 1
                continue
            else:
                # add number last line
                tmp.append(i-1)
                line_stm.append(tmp)
                # Break blok statement
                break
            # i += 1
        line += i
        print(cons, line_stm, line)
        # Convert variable to value
        for k in range(len(cons)):
            cons[k] = re.findall(key_word, cons[k])
            for i in range(len(cons[k])):
                for j in range(len(var)):
                    if cons[k][i] == var[j]:
                        cons[k][i] = in_var[j]
        # Cek value of cons
        for i in range(len(cons)):
            operation = Class_Condition(cons[i])
            if cons[i] is True:
                return line_stm[i]
            elif operation.Main() is True:
                return line_stm[i]
    # Helper
    def Nested(self, scan):
        scanned = re.split(r'(\s+)', scan)
        if len(scanned[1]) < 4:
            return 0
        nest = len(scanned[1])/4
        return nest