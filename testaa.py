import random
import prototype1

def randomizer():
    list = []
    for i in range(0, 4):
        x = random.randint(1, 13)
        list.append(x)
    return list

sca = 0
for i in range(0, 1000):
    list = randomizer()
    result = prototype1.algorithm24(list)
    score = prototype1.score24(result)
    print('Result = ', result)
    print('Score = ', score)
    sca += score

print('Total score = ', sca/1000)
