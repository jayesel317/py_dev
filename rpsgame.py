import random
import time

player = ['rock','paper','scissors','gun','machete','nuke']

for i in range(3):
    print(i+1)
    time.sleep(1)

print(random.choice(player))
