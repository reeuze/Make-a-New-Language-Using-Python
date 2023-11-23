import re
class Label:
    def __init__(self):
        self.Label = {}
        self.nest = 0
    # Main
    def Label_name(self, label, line):
        if 'ke' in label:
            return [False, self.nest]
        else:
            label = label.replace(':', '')
            self.Label.update({label:line})
            self.nest = self.Nested(label)
            return [True, self.nest]
    def Goto_statement(self, label, lines, line):
        statement = label.split()
        label = statement[1]
        if label in self.Label:
            return [self.Label[label], self.nest]
        else:
            label = label+':'
            i = line
            while i < len(lines):
                if label == lines[i]:
                    return [i, self.nest]
                i += 1
            return [-1, self.nest]
    # Helper
    def Nested(self, scan):
        scanned = re.split(r'(\s+)', scan)
        if len(scanned) == 1:
            return 0
        elif len(scanned[1]) < 4:
            return 0
        nest = len(scanned[1])/4
        return nest

    # Helper