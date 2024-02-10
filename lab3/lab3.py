def main():
    dict = {"а" :1, "б" :2, "в" :3, "г" :4, "д" :5, "е" :6, "ё" :7, "ж" :8, 
           "з" :9, "и" :10, "й" :11, "к" :12, "л" :13, "м" :14, "н" :15, "о" :16, 
           "п" :17, "р" :18, "с" :19, "т" :20, "у" :21, "ф" :22, "х" :23, "ц" :24, 
           "ч" :25, "ш" :26, "щ" :27, "ъ" :28, "ы" :29, "ь" :30, "э" :31, "ю" :32, 
           "я" :33}
    dict2 = {v: k for k, v in dict.items()}
    gamma = input("Введите гамму, состоящую из букв dict ").lower()
    text = input("Введите текст для шифрования ").lower()
    listtext = list()
    listgamma = list()
    for i in text:
        listtext.append(dict[i])
    print("Числа текста", listtext)
    for i in gamma:
        listgamma.append(dict[i])
    print("Числа гаммы", listgamma)
    listresult = list()
    ch = 0
    for i in text:
        try:
            a = dict[i] + listgamma[ch]
        except:
            ch = 0
            a = dict[i] + listgamma[ch]
        if a>=33:
            a = a%33
        ch += 1
        listresult.append(a)
    print("Числа зашифрованного текста", listresult)
    textencrypted = ""
    for i in listresult:
        textencrypted += dict2[i]
    print("Зашифрованный текст: ", textencrypted)
    listofdigits = list()
    for i in textencrypted:
        listofdigits.append(dict[i])
    ch = 0
    listofdigits1 = list()
    for i in listofdigits:
        a = i - listgamma[ch]
        if a < 1:
            a += 33
        listofdigits1.append(a)
        ch += 1
    textdecrypted = ''
    for i in listofdigits1:
        textdecrypted += dict2[i]
    print("Decrypted text", textdecrypted)


main()