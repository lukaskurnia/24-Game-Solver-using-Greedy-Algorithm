import prototype1
import random

def manualInput():
    str = input('Masukkan keempat angka yang membentuk 24!\n')
    numbers = str.split()
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    numbers[2] = int(numbers[2])
    numbers[3] = int(numbers[3])
    
    result = prototype1.algorithm24(numbers)
    score = prototype1.score24(result)
    print('Result = ', result)
    print('Score = ', score)

manualInput()
