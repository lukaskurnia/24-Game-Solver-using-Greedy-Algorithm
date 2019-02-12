#import random
import backend


'''def randomizer():
    list = []
    for i in range(0, 4):
        x = random.randint(1, 13)
        list.append(x)
    return list'''

sca = 0
#sca2 = 0
hit = 0
#hit2 = 0
#for i in range(0, 10000):
    #list = randomizer()
for i in range (1,14):
    for j in range (1,14):
        for k in range (1,14):
            for l in range (1,14):
                list = [i,j,k,l]
                #print(list)
                result = backend.algorithm24(list)
                #result2 = backproto2.algorithm24(list)
                #print('Result 2 = ', result2)

                score = backend.score24(result)
                #score2 = backproto2.score24(result2)
                #print('Score 2 = ', score2)
                #print()
                sca += score
                #sca2 += score2
                if (eval(result) == 24):
                    hit += 1
                '''if (eval(result2) == 24):
                    hit2 += 1'''
total = 13*13*13*13
print('Rata-Rata skor dan hit ke angka 24 menggunakan algoritma greedy dari 13^4 kemungkinan: ')
print('Total score = ', sca/total)
#print('Total score2 = ', sca2/10000)
print('Hit total = ', hit, '/' , total , '= ', (hit/total)*100, '%')
#print('Hit total 2 = ', hit2)
