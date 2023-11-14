import re
from .Logical_operation import Class_Condition
class Condition:
    def __init__(self):
        self_input = []
    # Main
    def Main(self, scan):
        operation = Class_Condition(scan)
    # Sub Main
    def If_stm(self):
        print('A')
    def Elif_stm(self):
        print('B')
    def Else_stm(self):
        print('C')
    # Helper