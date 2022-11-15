#1.#
def f(num):
    if num < 10:
        return -1
    else:
        sum = str(num)
    return int(sum[-2])
#2.#
def f(sum):
    sum1 = ''.join(filter(str.isalpha, sum)).lower()
    return sum1[::-1] == sum1
#3.#
def split(sum):
    return [char for char in sum]
def min_ch(sum):
    if sum > 0:
        per = 1
    else:
        per = -1
    sum = split(str(sum))
    sum= sorted(sum)
    for i in range(len(sum)):
        if int(sum[i]) > 0:
            l = i
            break
    print(sum)
    return int(sum[l] + "".join(sum[1:l]) + '0' + "".join(sum[l + 1:])) * p
#4.#
def split(sum):
    return [char for char in sum]
def min_ch(sum):
    if sum > 0:
        p = 1
    else:
        p = -1
    sum = split(str(sum))
    sum = sorted(sum)
    for i in range(len(sum)):
        if int(sum[i]) > 0:
            l = i
            break
    print(s)
    return int(sum[l] + "".join(sum[1:l]) + '0' + "".join(sum[l + 1:])) * p
#№1 numpy (file 2)#
import numpy as np
def n1(a: np.ndarray, b: np.ndarray):
    c = 0
    d = 0
    for i in range(len(a)):
        c = c+a[i]**2
        d = d+b[i]**2
    b = np.transpose(b)
    f = np.dot(a,b)/np.sqrt(c*d)
    return np.rad2deg(np.arccos(f))
#5.file2#
import numpy as np
def matrix(a: np.array, b: np.array):
    b = np.transpose(b)
    return a.dot(b)
#6.file2#
import numpy as np
def f (a: np.array, b: np.array):
    b1 = np.transpose(b)
    a1 = np.transpose(a)
    c = a.dot(b1)
    l = a.dot(a1)
    d = b.dot(b1)
    return np.arccos(c/(l*d))
#№10.#
def n10(sum):
    str = open(sum, "r").read().lower()
    f = {}
    n = 0
    for c in str:
       if ord('a') <= ord(c) <= ord('z'):
           x = f.get(c, 0)
           f[c] = x + 1
           n += 1
    for key in f:
        f[key] = f[key] / n
    return f
#№1.1#
import pandas as pd
f = pd.read_csv('use.csv')
d=dict()
# пункт 1
d['number_of students']=len(f[(~f['Математика'].isna())|(~f['Физика'].isna())]|(~f['Русский язык'].isna()))
# №2 из пдф-файла
import pandas as pd
def pandas_task2(a: np.ndarray, n: int) -> np.ndarray:
    b, c, d = a.split(".")
    td = datetime.date(int(b), int(c), int(d))
    sd = datetime.date(1, 1, 1)
    diff = sd - td
    diff = str(diff)
    return diff[1:diff.rfind(",")]
