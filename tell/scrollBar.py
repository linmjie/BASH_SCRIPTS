import sys

#style: [|||||||         ] 12/200 (12%)
#       ^                ^^      ^
#       |                ||      |
#    bracket       brackets and whitespaces

columns = int(sys.argv[1])
current = int(sys.argv[2])
max = int(sys.argv[3])

proportion = current/max

fraction = f"{current}/{max}"
percent = f"({int(proportion * 100)}%)"

#        (100%)  + max +           max + / + whitespace + brackets
takeOut = 6      + len(str(max)) * 2   + 1 + 2          + 2
maxBars = columns - takeOut

numBars = int(maxBars * proportion)
numEmpty = maxBars - numBars

print(f"[{numBars * '|'}{numEmpty * ' '}] {fraction} {percent}")
