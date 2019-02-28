from pyparsing import *


def get_parser():
    """
    A valid statement is the word "block:", followed by an indent, followed by the letter A only
    """
    stack = [1]
    body = indentedBlock(Literal('A'), indentStack=stack, indent=True)
    block = Literal('block:') + body
    return block


# This input string is a perfect match for the parser, so a single match is found
p1 = get_parser()
r1 = list(p1.scanString("""
block:
    A
"""))
assert len(r1) == 1

# This input string is a perfect match for the parser, except for the letter B instead of A, so this will fail (and should)
p2 = get_parser()
r2 = list(p2.scanString("""
block:
    B
"""))
assert len(r2) == 0

# This input string contains both string A and string B, and it finds one match (as it should)
p3 = get_parser()
r3 = list(p3.scanString("""
block:
    A
block:
    B
"""))
assert len(r3) == 1

# This input string contains both string A and string B, but in a different order.
# This means that the indented block matches, but then parsing fails because of the character B
# Then, because the indent stack is not unrolled back to [1], it fails to match the second block also
p4 = get_parser()
r4 = list(p4.scanString("""
block:
    B
block:
    A
"""))
assert len(r4) == 1
