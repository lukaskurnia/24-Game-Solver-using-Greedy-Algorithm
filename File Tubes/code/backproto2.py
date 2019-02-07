def algorithm24(list4):
    quickSort(list4, 0, 3)
    sol = str(list4[0]) + ' + ' + str(list4[1]) + ' + ' + str(list4[2]) + ' + ' + str(list4[3])

    if eval(sol) == 24:
        is24 = True
    else:
        is24 = False

    count = 0
    while (not is24 and count != 3):
        sol = changeOperator(sol)
        count+= 1

    sol = bracketVariant(sol)

    return sol

def changeOperator(expr):
    sol = expr
    if to24(sol) > 0:
        sol2 = sol
        for i in range(1, 4):
            newsol = changeOpr(sol, i, '+')
            if compare24(sol2, newsol):
                sol2 = newsol
        for i in range(1, 4):
            newsol = changeOpr(sol, i, '*')
            if compare24(sol2, newsol):
                sol2 = newsol
        sol = sol2

    elif to24(sol) < 0:
        sol2 = sol
        for i in range(1, 4):
            newsol = changeOpr(sol, i, '-')
            if compare24(sol2, newsol):
                sol2 = newsol
        for i in range(1, 4):
            newsol = changeOpr(sol, i, '/')
            if compare24(sol2, newsol):
                sol2 = newsol
        sol = sol2

    return sol

def bracketVariant(expr):
    sol = expr
    newsol = createBracket(expr, 0, 2)
    if compare24(sol, newsol):
        sol = newsol
    newsol = createBracket(expr, 0, 3)
    if compare24(sol, newsol):
        sol = newsol
    newsol = createBracket(expr, 1, 3)
    if compare24(sol, newsol):
        sol = newsol
    newsol = createBracket(expr, 1, 4)
    if compare24(sol, newsol):
        sol = newsol
    newsol = createBracket(expr, 2, 4)
    if compare24(sol, newsol):
        sol = newsol
    newsol = createBracket(expr, 0, 2)
    newsol = createBracket(newsol, 2, 4)
    if compare24(sol, newsol):
        sol = newsol
    return sol

def createBracket(expr, start, end):
    count = 0
    i = 0
    while (count != start):
        if expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
            count += 1
            i += 1
        else:
            i += 1
    expr = expr[:i] + '(' + expr[i:]
    if end == 4:
        expr = expr + ')'
    else:
        while(count != end):
            if expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
                count += 1
                i += 1
            else:
                i += 1
        i -= 1
        expr = expr[:i] + ')' + expr[i:]
    return expr

def changeOpr(expr, no, chg):
# Mengganti operator yang ke berapa dengan operator lain
    i = 0
    count = 0
    while (count != no):
        if expr[i] == '+' or expr[i] == '-' or expr[i] == '*' or expr[i] == '/':
            count += 1
            i += 1
        else:
            i += 1
    i -= 1
    newexpr = expr[:i] + chg + expr[(i + 1):]
    return newexpr

# Tester main program

def main():
    str = input('Masukkan keempat angka yang membentuk 24!\n')
    numbers = str.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    result = algorithm24(numbers)
    score = score24(result)
    print('Result = ', result)
    print('Score = ', score)


# Fungsi-fungsi pembantu

def to24(expr):
# Menghitung hasil ketika dikurangi angka 24
    to = 24 - eval(expr)
    return to

def dev24(expr):
# Menghitung jarak / deviasi ke angka 24
    dev = abs(24 - eval(expr))
    return dev

def compare24(expr1, expr2):
# Mengembalikan true jika dev24(expr2) lebih kecil
    if dev24(expr2) < dev24(expr1):
        return True
    else:
        return False


def score24(expr):
# Menghitung skor yang membentuk angka 24
    score = -1 * abs(24 - eval(expr))
    for i in range(len(expr)):
        if expr[i] == '+':
            score += 5
        elif expr[i] == '-':
            score += 4
        elif expr[i] == '*':
            score += 3
        elif expr[i] == '/':
            score += 2
        elif expr[i] == '(':
            score -= 1
    return score

def quickSortHelper(numlist, first, last):
# Mencari indeks yang benar buat quickSort
# Membantu mengurutkan partisi yang ada
    target = numlist[last]
    z = first - 1

    for i in range(first, last):
        if numlist[i] > target:
            z += 1
            numlist[i], numlist[z] = numlist[z], numlist[i]

    numlist[z + 1], numlist[last] = numlist[last], numlist[z + 1]
    return (z + 1)

def quickSort(numlist, first, last):
# Mengurutkan list dari besar ke kecil dengan quicksort
    if first < last:
        # Mencari indeks partisi
        part = quickSortHelper(numlist, first, last)
        # Mengurutkan
        quickSort(numlist, first, part - 1)
        quickSort(numlist, part + 1, last)

main()
