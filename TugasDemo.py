#################################################
#M. Izdiar Alnafisi Aryadi - 5024211015
#Run program dalam file .txt
#################################################
import math
#################################################
#inisialisasi variabel-varibel
#################################################
var = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0}
s_stack = []
s_output = []
perhitungan = []
kurung_buka = '({['
kurung_tutup = ')}]'
priority1 = '^'
priority2 = '*/:%'
priority3 = '+-'
operan = ""
hitung = []
hasil = 0

#################################################
#fungsi mencari operator
#################################################
def isOperator(str):
    if '^' in str or '*' in str or '/' in str or ':' in str or '%' in str or '+' in str or '-' in str :
        return True
    else:
        return False
    

#################################################
#fungsi mencari lokasi char tertentu
#################################################
def locateChar(str,char):
    n=0
    for i in str:
        if i == char:
            return n
        n += 1

#################################################
#fungsi mencocokkan variabel
#################################################
def returnVar(char):
    if char == 'a':
        return var['a']
    if char == 'b':
        return var['b']
    if char == 'c':
        return var['c']
    if char == 'd':
        return var['d']
    if char == 'e':
        return var['e']
    if char == 'f':
        return var['f']
    if char == 'g':
        return var['g']
    if char == 'h':
        return var['h']
    if char == 'i':
        return var['i']

#################################################
#fungsi mengganti float ke int apabila tidak pecahan
#################################################
def toInt(x):
    if x-math.floor(x) == 0:
        return int(x)
    else:
        return x

#################################################
#fungsi input nilai variabel
#################################################
def inputVar(char,inVal):
    inVal = toInt(inVal)
    if char == 'a':
        var['a'] = inVal
    if char == 'b':
        var['b'] = inVal
    if char == 'c':
        var['c'] = inVal
    if char == 'd':
        var['d'] = inVal
    if char == 'e':
        var['e'] = inVal
    if char == 'f':
        var['f'] = inVal
    if char == 'g':
        var['g'] = inVal
    if char == 'h':
        var['h'] = inVal
    if char == 'i':
        var['i'] = inVal

#################################################
#konversi ke float
#################################################
def toFloat(str):
    if str.isnumeric():
        return float(str)
    elif str.isalpha():
        return returnVar(str)
    
#################################################
#cek prioritas operator
#################################################
def priority_cek(x,y):
    if (x in priority1 and (y in priority1 or y in priority2 or y in priority3)) or (x in priority2 and (y in priority2 or y in priority3))or (x in priority3 and y in priority3):
        return True
    else:
        return False

#################################################
#fungsi perhitungan
#################################################
def menghitung(operator, operan1, operan2):
    if operator == '+':
        return operan1 + operan2
    elif operator == '-':
        return operan1 - operan2
    elif operator == '*':
        return operan1 * operan2
    elif operator == '%':
        return operan1 % operan2
    elif operator == '/' or operator == ':':
        if operan2 == 0:
            print('Tidak bisa membagi dengan nol')
            quit()
        return operan1 / operan2
    elif operator == '^':
        return operan1 ** operan2

#################################################
#fungsi kalkulator
#################################################
def Calc(str):
    global operan, hasil
    for i in range(len(str)):
        if str[i].isnumeric() or str[i].isalpha():
            operan += str[i]
        elif str[i] in kurung_buka:
            if len(operan) != 0 :
                s_output.append(operan)
                perhitungan.append(operan)
                operan = ""
            s_stack.append(str[i])
        elif str[i] in kurung_tutup:
            if len(operan) != 0 :
                s_output.append(operan)
                perhitungan.append(operan)
                operan = ""
            x=len(s_stack)
            for j in range(len(s_stack)):
                if s_stack[x-j-1] in kurung_buka:
                    s_stack.pop()
                    break
                else:
                    s_output.append(s_stack[-1])
                    perhitungan.append(s_stack.pop())
        elif str[i] in priority1 or str[i] in priority2 or str[i] in priority3:
            if len(operan) != 0 :
                s_output.append(operan)
                perhitungan.append(operan)
                operan = ""
            if len(s_stack) != 0:
                if priority_cek(s_stack[-1],str[i]):
                    s_output.append(s_stack[-1])
                    perhitungan.append(s_stack.pop())
            s_stack.append(str[i])
    #output sisa pada operan dan s_stack
    if len(operan) != 0 :
        s_output.append(operan)
        perhitungan.append(operan)
        operan = ""
    for i in range(len(s_stack)):
        if len(s_stack) != 0:
                for i in range(len(s_stack)):
                    s_output.append(s_stack[-1])
                    perhitungan.append(s_stack.pop())
    #program penghitung
    #print(perhitungan)
    for i in perhitungan:
        if i.isnumeric():
            hitung.append(float(i))
        elif i.isalpha():
            hitung.append(float(returnVar(i)))
            #print(hitung)
        elif i in priority1 or i in priority2 or i in priority3:
            if len(hitung) < 2:
                print('perthitungan tidak dapat dilakukan')
                quit()
            operan2 = hitung.pop()
            operan1 = hitung.pop()
            hasil = menghitung(i, operan1, operan2)
            #print(hasil)
            hitung.append(hasil)
        else:
            print('perthitungan tidak dapat dilakukan')
            quit()
    return hasil

#################################################
#fungsi perintah cetak
#################################################
def cetak(str):
    x=""
    m = locateChar(str,'(')
    n = locateChar(str,')')
    x = str[m+1:n]
    #print(len(x))
    if len(x) == 1:
        print(returnVar(x))
    elif chr(34) in x:
        print(x[1:len(x)-1])
    else:
        print(x)

#################################################
#fungsi cek kondisi pada if
#################################################
def conCek(str):
    if ">=" in str:
        n = locateChar(str,'>')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+2:])
        if operan1 >= operan2:
            return True
        else:
            return False
    elif "<=" in str:
        n = locateChar(str,'<')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+2:])
        if operan1 <= operan2:
            return True
        else:
            return False
    elif "==" in str:
        n = locateChar(str,'=')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+2:])
        if operan1 == operan2:
            return True
        else:
            return False
    elif "!=" in str:
        n = locateChar(str,'!')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+2:])
        if operan1 != operan2:
            return True
        else:
            return False
    elif ">" in str:
        n = locateChar(str,'>')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+1:])
        if operan1 > operan2:
            return True
        else:
            return False
    elif "<" in str:
        n = locateChar(str,'<')
        operan1 = toFloat(str[:n])
        operan2 = toFloat(str[n+1:])
        if operan1 < operan2:
            return True
        else:
            return False
    else:
        print("operasi pada kondisi tidak memenuhi")

#################################################
#fungsi perintah jika
#################################################
def jika(list,str,n):
    #print(str)
    m = locateChar(str,'(')
    n = locateChar(str,')')
    condition = str[m+1:n]
    #print(condition)
    #o = locateChar(str,' ')
    statement = str[n+1:]
    #print(statement)
    if conCek(condition):
        lineExe(list,statement,n)

#################################################
#fungsi perintah goto
#################################################
def goto(list,str):
    oPertama = locateChar(str,'o')
    for i in range(len(str)-oPertama):
        if str[i+oPertama] == ' ':
            n = i+oPertama+1
    label = str[n:]
    for i in range(len(list)):
        if label in list[i]:
            labelLoc = i
            break
    return labelLoc

#################################################
#fungsi untuk input nilai var dan perhitungan
#################################################
def Kalkulasi(str):
    n = locateChar(str,'=')
    dihitung = str[n+1:]
    hasil = Calc(dihitung)
    inputVar(str[0],hasil)

#################################################
#fungsi untuk cek perintah pada line
#################################################
def isFunction(str):
    if "cetak" in str or "jika" in str or "goto" in str:
        return True
    else:
        return False


#################################################
#fungsi eksekusi line yang dibaca
#################################################
def lineExe(list,strCek,lokasi):
    if isFunction(strCek):
        if "jika" in strCek:
            jika(list,strCek,lokasi)
        elif "cetak" in strCek:
            cetak(strCek)
        elif "goto" in strCek:
            label = goto(list,strCek)
            #dfunc = lokasi-label-1
            #print(lokasi)
            #print(list[label:dfunc])
            mainFunction(list[label:])
    elif "=" in strCek:
        if isOperator(strCek):
            Kalkulasi(strCek)
        else :
            n = locateChar(strCek,'=')
            variabel = strCek[:n]
            value = float(strCek[n+1:])
            inputVar(variabel,value)
    else :
        pass

#################################################
#program utama
#################################################
def mainFunction(lines):
    for i in range(len(lines)):
        #print(i)
        lineExe(lines,lines[i],i)


file = open('run.txt','r').read()

line_list = file.split('\n')
mainFunction(line_list)
