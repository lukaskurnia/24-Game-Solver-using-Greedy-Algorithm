f = open("test.txt","r")

for x in f:
  number = list(x.split(' '))
  number[0] = float(number[0])
  number[1] = float(number[1])
  number[3] = float(number[3])
  number[2] = float(number[2])
  print(number[0]+number[1])

f = open("answer.txt","w")
s = str(number[0]) + str(number[1])
f.write(s) #harus dalam string
