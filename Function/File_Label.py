class Label:
    def __init__(self):
        self.Label = {}
    def Label_name(self, label, line):
        self.Label.update({label:line})
        return True
    def Goto_statement(self, label, lines, line):
        statement = label.split()
        label = statement[1]
        name_label = label.replace(':', '')
        if name_label in self.Label:
            return self.Label[label]
        else:
            i = line
            while lines:
                if label == lines[i]:
                    return i
                else:
                    return -1
                i += 1

    # Helper