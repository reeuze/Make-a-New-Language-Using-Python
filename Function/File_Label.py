class Label:
    def __init__(self):
        self.Label = {}
    def Label_name(self, label, line):
        if 'goto' in label:
            return False
        label = label.replace(':', '')
        self.Label.update({label:line})
        return True
    def Goto_statement(self, label, lines, line):
        statement = label.split()
        label = statement[1]
        if label in self.Label:
            return self.Label[label]
        else:
            label = label+':'
            i = line
            while lines:
                i += 1
                if label == lines[i]:
                    return i
            return -1

    # Helper