def algorithm24(list4):
    # Tahap 0: Sorting dahulu list
    sort24(list4)
    print(list4)

    # Tahap 1: Mencari nilai score24 max dari 2 angka terbesar
    sol1 = solve2(list4)

    # Tahap 2: Mencari nilai score24 dari 3 angka
    sol2 = solve3(list4[2], sol1)

    # Tahap 3: Mencari nilai score24 dari 4 angka
    sol3 = solve3(list4[3], sol2)

    return sol3

def sort24(list4):
# Bubble Sort dari terbesar ke terkecil
    for i in range(len(list4)):
        for j in range(len(list4) - i - 1):
            if list4[j]<list4[j+1]:
                list4[j], list4[j+1] = list4[j+1], list4[j]

def solve2(list4):
# Mencari operasi 2 bilangan agar mencapai angka 24
    a = list4[0]
    b = list4[1]
    str1 = str(a) + '+' + str(b)
    str2 = str(a) + '-' + str(b)
    str3 = str(a) + '*' + str(b)
    str4 = str(a) + '/' + str(b
    res = str1
    if (score24(str2) >= score24(res)):
        res = str2
    if (score24(str3) >= score24(res)):
        res = str3
    if (score24(str4) >= score24(res)):
        res = str4
    return res

def solve3(c, sol):
# Mencari operasi 3 angka atau 4 angka yang menghasilkan nilai skor maksimum
    str1 = sol + '+' + str(c)
    str2 = sol + '-' + str(c)
    str3 = str(c) + '-' + sol
    str4 = sol + '*' + str(c)
    str5 = sol + '/' + str(c)
    str6 = str(c) + '*' + sol
    str7 = str(c) + '/' + sol
    str8 = '(' + sol + ')*' + str(c)
    str9 = '(' + sol + ')/' + str(c)
    str10 = str(c) + '/(' + sol + ')'

    res = str1
    if (score24(str2) >= score24(res)):
        res = str2
    if (score24(str3) >= score24(res)):
        res = str3
    if (score24(str4) >= score24(res)):
        res = str4
    if (score24(str5) >= score24(res)):
        res = str5
    if (score24(str6) >= score24(res)):
        res = str6
    if (score24(str7) >= score24(res)):
        res = str7
    if (score24(str8) >= score24(res)):
        res = str8
    if (score24(str9) >= score24(res)):
        res = str9
    if (score24(str10) >= score24(res)):
        res = str10
    return res

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
