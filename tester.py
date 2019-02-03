import prototype1
import random

def manualInput():
    str = input('Masukkan keempat angka yang membentuk 24!\n')
    numbers = str.split()
    result = prototype1.algorithm24(numbers)
    score = prototype1.score24(result)
    print('Result = ', result)
    print('Score = ', score)

manualInput()
