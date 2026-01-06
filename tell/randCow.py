#cowsay
import random
import sys

#Cow files in /usr/share/cowsay/cows: apt bud-frogs bunny
#                                   ^
#                                   |
#Everything left of this is not needed, now a valid cow
#Apparently this left side doesn't generate in the subshell... sometimes
optCows = input().split(':')
cows = optCows
try:
    cows = optCows[1].split()
except: 
    cows = optCows[0].split()

cow = random.choice(cows)
print(cow)
#sys.stderr.write(cow + '\n')
