links = [link.strip().split(')') for link in open('6.in').readlines()]

M = {h: [] for h in set(l[0] for l in links)}

for l in links:
    M[l[0]].append(l[1])

def count_links_r(obj, d):
    sum = d
    if obj in M.keys():
        for orb in M[obj]:
            sum += count_links_r(orb, d+1)
    return sum

print(count_links_r('COM', 0))
