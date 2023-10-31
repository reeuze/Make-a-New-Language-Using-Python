class Label:
    def __init__(self):
        self.Label = {}
    # Label Type
    def Label_name(self, label, line):
        if 'ke' in label:
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
            while i < len(lines):
                if label == lines[i]:
                    return i
                i += 1
            return -1

    # Helper