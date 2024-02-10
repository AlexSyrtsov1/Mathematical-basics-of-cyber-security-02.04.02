import sys

def prints(lists):
    for i in lists:
        for j in i:
            print(j, end = " ")
        print()

def delete(largelist,inn,k):
    for i in range(k*2):
        for j in range(k*2):
            if largelist[i][j] == inn:
                largelist[i][j] = ' '
                return

def povorot(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def reshetka():
    k = int(input('Введите k '))
    s = 1
    lists = [[i for i in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):
            lists[i][j] = s
            s += 1
    print(lists)
    lists1 = povorot(lists)
    lists2 = povorot(lists1)
    lists3 = povorot(lists2)
    largelist = [[1 for i in range(2*k)] for i in range(2*k)]
    for i in range(k):
        for j in range(k):
            largelist[i][j] = lists[i][j]
    i1 = 0
    j1 = 0
    for i in range(0, k):
        for j in range(k, k*2):
            largelist[i][j] = lists1[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    i1 = 0
    j1 = 0
    for i in range(k, k*2):
        for j in range(k, k*2):
            largelist[i][j] = lists2[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    i1 = 0
    j1 = 0
    for i in range(k, k*2):
        for j in range(0, k):
            largelist[i][j] = lists3[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    prints(largelist)
    text = 'договорподписали'
    largelist1 = [[' ' for i in range(2*k)] for i in range(2*k)]
    s = 0
    li = [i for i in range(1, k**2 + 1)]
    for inn in li:
        delete(largelist, inn, k)
    ind = 0
    for i in range(k*2):
        for j in range(k*2):
            if largelist[i][j] == largelist1[i][j] and len(text) > 0:
                largelist1[i][j] = text[0]
                text = text[1:]
    largelist = povorot(largelist)
    for i in range(k*2):
        for j in range(k*2):
            if largelist[i][j] == largelist1[i][j] and len(text) > 0:
                largelist1[i][j] = text[0]
                text = text[1:]
    if len(text) > 0:
        largelist = povorot(largelist)
        for i in range(k*2):
            for j in range(k*2):
                if largelist[i][j] == largelist1[i][j] and len(text) > 0:
                    largelist1[i][j] = text[0]
                    text = text[1:]
    if len(text) > 0:
        largelist = povorot(largelist)
        for i in range(k*2):
            for j in range(k*2):
                if largelist[i][j] == largelist1[i][j] and len(text) > 0:
                    largelist1[i][j] = text[0]
                    text = text[1:]
    prints(largelist1)
    string = input('Введите пароль ')
    if len(string) > k*2:
        string = string[:k*2]
    elif len(string) < k*2:
        while len(string) != k*2:
            string += 'z'
    largelist1.append(list(string))
    prints(largelist1)
    result = ''
    spisok = sorted(largelist1[len(largelist1) - 1])
    for i in spisok:
        print(i, ' = ', largelist1[len(largelist1) - 1].index(i))
        for j in range(len(largelist1)):
            if j == len(largelist1) - 1:
                continue
            result += largelist1[j][largelist1[len(largelist1) - 1].index(i)]
    print(result.replace(' ', ''))

reshetka()