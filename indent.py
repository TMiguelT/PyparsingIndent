from pyparsing import *


def get_parser():
    stack = [1]
    body = indentedBlock(Literal('A'), indentStack=stack, indent=True)
    block = Literal('block:') + body
    return block


p1 = get_parser()
r1 = list(p1.scanString("""
block:
    A
"""))

assert len(r1) == 1

p2 = get_parser()
r2 = list(p2.scanString("""
block:
    B
"""))

assert len(r2) == 0

p3 = get_parser()
r3 = list(p3.scanString("""
block:
    B
block:
    A
"""))

assert len(r3) == 1
