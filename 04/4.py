from itertools import groupby

def check(n):
    ans = False
    nl = list(map(int, list(str(n))))
    i = 0
    while not ans and i < 5:
        if nl[i] == nl[i+1]:
           ans = True
        i += 1

    i = 0
    while ans and i < 5:
        if nl[i] > nl[i+1]:
            ans = False
        i += 1

    return ans

def counts(n):
    nl = list(map(int, list(str(n))))
    return [len(list(group)) for key,group in groupby(nl)]

l,r = tuple(map(int, open('4.in').read().strip().split('-')))

ps = []
count = 0
for num in range(l,r):
    if check(num):
       ps.append(num)

new_ps = []
for p in ps:
    if 2 in counts(p):
        new_ps.append(p)

print(len(new_ps))
