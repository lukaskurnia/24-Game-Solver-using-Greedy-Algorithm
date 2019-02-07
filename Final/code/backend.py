def algorithm24(list4):
#Fungsi utama yang mengembalikan ekspresi hasil algoritma greedy
    list4.sort(reverse= True)
    #List angka diurut secara menurun dari maksimum ke minimum
    sol = str(list4[0]) + ' + ' + str(list4[1]) + ' + ' + str(list4[2]) + ' + ' + str(list4[3])
    #default awal ekspresi adalah a+b+c+d

    if eval(sol) == 24:
        is24 = True
    else: #Jika tidak mencapai 24, urutan operator dimainkan
        is24 = False
        count = 0
        while (not is24 and count != 3):
        #Pengulangan berhenti ketika mencapai 24 atau telah diulang 3x untuk tempat operator berbeda
            sol = changeOperator(sol)
            count+= 1
        if eval(sol) != 24:
        #Mencoba mencari optimum dengan menambahkan tanda kurung
            sol = bracketVariant(sol)

    return sol

def changeOperator(expr):
    sol = expr
    if to24(sol) > 0:
    #jika nilai ekspresi <24 maka ditambahkan atau dikali untuk mendekati 24 (mencari optimum)
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
    #jika nilai ekspresi >24 maka ditambahkan atau dikali untuk mendekati 24 (mencari optimum)
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
#Variasi kurung:
# (a+b)+c+d
# (a+b+c)+d
# a+(b+c)+d
# a+(b+c+d)
# a+b+(c+d)
# (a+b)+(c+d)
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
