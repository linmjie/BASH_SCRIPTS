#cowsay
import random
import sys

#Cow files in /usr/share/cowsay/cows: apt bud-frogs bunny
#                                   ^
#                                   |
#Everything left of this is not needed, now a valid cow
cows = input().split(':')[1].split()

cow = random.choice(cows)
print(cow)
#sys.stderr.write(cow + '\n')
