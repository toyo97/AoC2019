from math import ceil

R = {}

for line in open('14.in').readlines():
    reaction = line.strip().split(' => ')
    for r in reaction[0].split(', '):
        n, r = r.split(' ')
        m, p = reaction[1].split(' ')
        R[(int(n),r)] = (int(m), p)


start = 'FUEL'

def get_res(prod_name, prod_qty):
    if prod_name == 'ORE':
        return(prod_qty)
    for n,r in R:
        if R[(n,r)][1] == prod_name:
            print(n,r)
            if R[(n,r)][0] >= prod_qty:
                return get_res(r,n)
            else:
                required = ceil(prod_qty / R[(n,r)][0]) * R[(n,r)][0]
                return get_res(r, required)

print(get_res(start, 1))

