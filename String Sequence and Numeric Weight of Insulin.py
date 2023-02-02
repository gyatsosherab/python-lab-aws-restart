"""
String Sequence and Numeric Weight of Insulin
"""
#Exercise 1: Assigning variables to the sequence elements of human insulin

# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

#Exercise 3: Using print() to display sequences of human insulin to the console

print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)
print("The sequence of human insulin, chain b " + bInsulin)
print("The sequence of human insulin, chain c" + cInsulin)
print("The sequence of human insulin, chain a and b" + insulin)