with open('out.csv') as f:
    s = f.readlines()
n = []
p = []
doms = {}
for i in range(1, len(s)):
    a = s[i].split(',')
    b = a[2]
    c = b.split('@')
    domen = c[1]
    if domen in doms:
        doms[domen] += 1
    else:
        doms[domen] = 1
a = []
for key, value in doms.items():
    a.append([key, value])

def BubbleSort(s):
    for i in range(0, len(s)-1):
        for j in range(0, len(s)-i-1):
            if s[j][1] < s[j+1][1]:
                temp = s[j]
                s[j] = s[j+1]
                s[j+1] = temp
    return s


a = BubbleSort(a)
print(a)

with open('answer.csv', 'w') as file:
    for el in a:
        file.write(f'{el[0]},{el[1]}\n')

