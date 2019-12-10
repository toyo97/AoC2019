def multiple(dx, dy, dvx, dvy):
    return dx/dy == dvx/dvy

# true if b is visible to a
def is_visible(b, a):
    dx, dy = b[0] - a[0], b[1] - a[1]

    for v in ast[a]:
        dvx, dvy = v[0] - a[0], v[1] - a[1]

        if dx == dvx == 0:
            if dy * dvy >= 0:
                return False
        elif dy == dvy == 0:
            if dx * dvx >= 0:
                return False
        elif dx * dvx > 0 and dy * dvy > 0 and multiple(dx, dy, dvx, dvy):
            return False
#    if a == (1,2) and b == (3,2):
#        print(ast[a])
    return True

def dist(tup):
    dx, dy = tup[0] - a[0], tup[1] - a[1]
    return abs(dx) + abs(dy)

lines = open('10.in').read().strip().split('\n')
chars = []
for line in lines:
    chars.append(list(line))

m = len(chars)
n = len(chars[0])

ast = {}

for i in range(m):
    for j in range(n):
        if chars[i][j] == '#':
            ast[(j,i)] = set()

for a in ast.keys():
    sorted_ast = sorted(ast.keys(), key=dist)

    for b in sorted_ast:
        if a != b and is_visible(b, a):
            ast[a].add(b)

counts = {a: len(s) for a,s in ast.items()}

best_ast = max(counts.keys(), key=lambda k: counts[k])
print(best_ast, counts[best_ast])
print(ast[best_ast])
