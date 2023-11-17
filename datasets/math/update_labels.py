# Takes a CSV with labels corresponding to the answer of the math
# problem in stdin, and outputs a csv wtih labels corresponding to the
# structure of the math problem. Expected format:

# statements,labels
# <statement1>,<label1>
# ...
# <statementN>,<labelN>


import sys

from data_gen import classify

for line in sys.stdin:
    print(line) # leave header unchanged
    break

for line in sys.stdin:
    statement=line.split(",")[0]
    print(f"{statement},{classify(statement)}")
