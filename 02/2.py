with open('2.in', 'r') as f:
    m = list(map(int, f.read().strip().split(',')))

#v = [30,1,1,4,2,5,6,0,99]

solution = 19690720

# candidates
c = [(a,b) for a in range(100) for b in range(100)]

for p in c:
    v = m[:]
    v[1] = p[0]
    v[2] = p[1]

    for i in range(0,len(v), 4):
        if v[i] == 1:
           v[v[i+3]] = v[v[i+1]] + v[v[i+2]]
        elif v[i] == 2:
            v[v[i+3]] = v[v[i+1]] * v[v[i+2]]
        elif v[i] == 99:
            break
    #    print(v)

    if v[0] == solution:
        print(100 * p[0] + p[1])
        break

