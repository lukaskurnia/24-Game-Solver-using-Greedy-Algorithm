import random
import backproto1
import backproto2

def randomizer():
    list = []
    for i in range(0, 4):
        x = random.randint(1, 13)
        list.append(x)
    return list

sca = 0
sca2 = 0
hit = 0
hit2 = 0
for i in range(0, 10):
    list = randomizer()
    result = backproto1.algorithm24(list)
    result2 = backproto2.algorithm24(list)
    print('Result 2 = ', result2)

    score = backproto1.score24(result)
    score2 = backproto2.score24(result2)
    print('Score 2 = ', score2)
    print()
    sca += score
    sca2 += score2
    if (eval(result) == 24):
        hit += 1
    if (eval(result2) == 24):
        hit2 += 1

print('Total score = ', sca/10000)
print('Total score2 = ', sca2/10000)
print('Hit total = ', hit)
print('Hit total 2 = ', hit2)
