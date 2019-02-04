# Nama  : Lukas Kurnia Jonathan
# NIM   : 13517006
# Tugas Kecil Strategi Algoritma, " 24 Game Solver"
import time #digunakan untuk mendapatkan waktu eksekusi program

print('________    _____     _________      .__                    ')
print('\_____  \  /  |  |   /   _____/ ____ |  |___  __ ___________')
print(' /  ____/ /   |  |_  \_____  \ /  _ \|  |\  \/ // __ \_  __ \'')
print('/       \/    ^   /  /        (  <_> )  |_\   /\  ___/|  | \'')
print('\_______ \____   |  /_______  /\____/|____/\_/  \___  >__|  ')
print('        \/    |__|          \/                      \/      ')
print('___.               .____           __                       ')
print('\_ |__ ___.__. /\  |    |    __ __|  | _______    ______    ')
print(' | __ <   |  | \/  |    |   |  |  \  |/ /\__  \  /  ___/    ')
print(' | \_\ \___  | /\  |    |___|  |  /    <  / __ \_\___ \     ')
print(' |___  / ____| \/  |_______ \____/|__|_ \(____  /____  >    ')
print('     \/\/                  \/          \/     \/     \/  ')

print('Please Enter your 4 numbers below,  (for example 4 7 8 8)')
S = input('>> ')
number = S.split()
#Bagian validasi input masukkan
while((len(number) != 4) or (int(number[0]) < 0) or (int(number[1]) < 0) or (int(number[2]) < 0) or (int(number[3]) < 0) ):
    print('Masukkan harus 4 angka dan bernilai positif')
    S = input('>> ')
    number = S.split()

start_time = time.time() #Waktu mulai dihitung ketika input sudah valid
a = (int(number[0]))
b = (int(number[1]))
c = (int(number[2]))
d = (int(number[3]))
#a,b,c,d diassign dengan input yang pengguna masukkan

def safe_div(x,y): #fungsi untuk melakukan pembagian yang aman, mengatasi ZeroDivision
    if(y==0):
        return 0
    else:
        return x/y

def hitungOperasi(a,b,c,d,op1,op2,op3,bracket): #fungsi untuk menghasilkan operasi matematika sesuai kurung
    hasil=0
    hasil2=0
    if(bracket ==0): #Tipe kurung pertama
        if(op1 == 0): hasil= a+b
        elif(op1 == 1):hasil= a-b
        elif(op1 == 2):hasil= safe_div(a,b)
        else:hasil= a*b

        if(op2 == 0):hasil+= c
        elif(op2 == 1):hasil-= c
        elif(op2 == 2):hasil = safe_div(hasil,c)
        else:hasil *= c

        if(op3 == 0):hasil+= d
        elif(op3 == 1):hasil-= d
        elif(op3 == 2):hasil = safe_div(hasil,d)
        else:hasil *= d

    if(bracket ==1): #Tipe kurung kedua
        if(op2 == 0):hasil= b+c
        elif(op2 == 1):hasil= b-c
        elif(op2 == 2):hasil= safe_div(b,c)
        else:hasil= b*c

        if(op1 == 0):hasil+= a
        elif(op1 == 1):hasil= a - hasil
        elif(op1 == 2):hasil = safe_div(a,hasil)
        else:hasil *= a

        if(op3 == 0):hasil+= d
        elif(op3 == 1):hasil-= d
        elif(op3 == 2):hasil = safe_div(hasil,d)
        else:hasil *= d

    if(bracket ==2): #Tipe kurung ketiga
        if(op2 == 0):hasil= b+c
        elif(op2 == 1):hasil= b-c
        elif(op2 == 2):hasil= safe_div(b,c)
        else:hasil= b*c

        if(op3 == 0):hasil+= d
        elif(op3 == 1):hasil-= d
        elif(op3 == 2):hasil = safe_div(hasil,d)
        else:hasil *= d

        if(op1 == 0):hasil+= a
        elif(op1 == 1):hasil= a - hasil
        elif(op1 == 2):hasil = safe_div(a,hasil)
        else:hasil *= a

    if(bracket ==3): #Tipe kurung keempat
        if(op3 == 0):hasil= c+d
        elif(op3 == 1):hasil= c-d
        elif(op3 == 2):hasil= safe_div(c,d)
        else:hasil= c*d

        if(op2 == 0):hasil+= b
        elif(op2 == 1):hasil= b-hasil
        elif(op2 == 2):hasil = safe_div(b,hasil)
        else:hasil *= b

        if(op1 == 0):hasil+= a
        elif(op1 == 1):hasil= a - hasil
        elif(op1 == 2):hasil = safe_div(a,hasil)
        else:hasil *= a

    if(bracket ==4): #Tipe kurung kelima
        if(op1 == 0):hasil= a+b
        elif(op1 == 1):hasil= a-b
        elif(op1 == 2):hasil= safe_div(a,b)
        else:hasil= a*b

        if(op3 == 0):hasil2 = c+d
        elif(op3 == 1):hasil2 = c-d
        elif(op3 == 2):hasil2 = safe_div(c,d)
        else:hasil2 = c*d

        if(op2 == 0):hasil+= hasil2
        elif(op2 == 1):hasil -= hasil2
        elif(op2 == 2):hasil = safe_div(hasil,hasil2)
        else:hasil *= hasil2

    return hasil

def InsertList(List,a,b,c,d,op1,op2,op3,bracket): #prosedur untuk mengupdate isi list
    if(op1==0): sign1 = '+'
    elif(op1==1): sign1 = '-'
    elif(op1==2): sign1 = '/'
    else:sign1 = '*'

    if(op2==0): sign2 = '+'
    elif(op2==1): sign2 = '-'
    elif(op2==2): sign2 = '/'
    else:sign2 = '*'

    if(op3==0): sign3 = '+'
    elif(op3==1): sign3 = '-'
    elif(op3==2): sign3 = '/'
    else:sign3 = '*'

    if(bracket==0): #Jenis kurung ke-1
        temp = '((' + str(a) +sign1 +str(b) + ')' +sign2 + str(c) + ')' +sign3 +str(d)
    elif(bracket==1): #Jenis kurung ke-2
        temp = '(' + str(a) +sign1 +'(' + str(b)  +sign2 + str(c)+'))' +sign3 +str(d)
    elif(bracket==2): #Jenis kurung ke-3
        temp =  str(a) +sign1 +'(('+str(b) +sign2 + str(c) + ')' +sign3 + str(d)+ ')'
    elif(bracket==3): #Jenis kurung ke-4
        temp =  str(a) +sign1 + '(' +str(b)  +sign2 + '('+str(c) +sign3 +str(d) + '))'
    else: #Jenis kurung ke-5
        temp = '(' + str(a) +sign1 +str(b) + ')' +sign2 + '(' +str(c) +sign3 +str(d) +')'

    if(temp not in List):
        List.append(temp) #memasukkan string ke dalam list

def solusibruteforce(List):
    return List[0]

solusi = []
for i in range(4): #loop untuk operator
    for j in range(4): #loop untuk operator
        for k in range (4): #loop untuk operator
            for l in range(5): #loop untuk tipe kurung
                if(abs(hitungOperasi(a,b,c,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,b,c,d,i,j,k,l)
                if(abs(hitungOperasi(a,b,d,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,b,d,c,i,j,k,l)
                if(abs(hitungOperasi(a,c,b,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,c,b,d,i,j,k,l)
                if(abs(hitungOperasi(a,c,d,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,c,d,b,i,j,k,l)
                if(abs(hitungOperasi(a,d,b,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,d,b,c,i,j,k,l)
                if(abs(hitungOperasi(a,d,c,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,a,d,c,b,i,j,k,l)

                if(abs(hitungOperasi(b,a,c,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,a,c,d,i,j,k,l)
                if(abs(hitungOperasi(b,a,d,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,a,d,c,i,j,k,l)
                if(abs(hitungOperasi(b,c,a,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,c,a,d,i,j,k,l)
                if(abs(hitungOperasi(b,c,d,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,c,d,a,i,j,k,l)
                if(abs(hitungOperasi(b,d,a,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,d,a,c,i,j,k,l)
                if(abs(hitungOperasi(b,d,c,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,b,d,c,a,i,j,k,l)

                if(abs(hitungOperasi(c,a,b,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,a,b,d,i,j,k,l)
                if(abs(hitungOperasi(c,a,d,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,a,d,b,i,j,k,l)
                if(abs(hitungOperasi(c,b,a,d,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,b,a,d,i,j,k,l)
                if(abs(hitungOperasi(c,b,d,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,b,d,a,i,j,k,l)
                if(abs(hitungOperasi(c,d,a,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,d,a,b,i,j,k,l)
                if(abs(hitungOperasi(c,d,b,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,c,d,b,a,i,j,k,l)

                if(abs(hitungOperasi(d,a,b,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,a,b,c,i,j,k,l)
                if(abs(hitungOperasi(d,a,c,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,a,c,b,i,j,k,l)
                if(abs(hitungOperasi(d,b,a,c,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,b,a,c,i,j,k,l)
                if(abs(hitungOperasi(d,b,c,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,b,c,a,i,j,k,l)
                if(abs(hitungOperasi(d,c,a,b,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,c,a,b,i,j,k,l)
                if(abs(hitungOperasi(d,c,b,a,i,j,k,l)-24) < 0.000000000001):
                    InsertList(solusi,d,c,b,a,i,j,k,l)
'''for answer in solusi: #Menampilkan solusi ke layar
    print(answer)'''

string = solusibruteforce(solusi)
print(string)
print('Jumlah solusi yang didapat adalah: ',len(solusi))
print("Program's execution time: %s seconds" % (time.time() - start_time))
