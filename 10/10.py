from collections import deque

def multiple(dx, dy, dvx, dvy):
    return dx/dy == dvx/dvy

# true if b is visible to a
def is_visible(b, a, ast_copy, dir=None):
    dx, dy = b[0] - a[0], b[1] - a[1]

    for v in ast_copy[a]:
        dvx, dvy = v[0] - a[0], v[1] - a[1]

        if dx == dvx == 0 and dy * dvy >= 0:
            if dir is not None:
                dir[v].append(b)
            return False
        elif dy == dvy == 0 and dx * dvx >= 0:
            if dir is not None:
                dir[v].append(b)
            return False
        elif dx * dvx > 0 and dy * dvy > 0 and multiple(dx, dy, dvx, dvy):
            if dir is not None:
                dir[v].append(b)
            return False
    if dir is not None:
        dir[b] = deque([b])
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

# ********** PART 1 **********

ast = {}

for i in range(m):
    for j in range(n):
        if chars[i][j] == '#':
            ast[(j,i)] = []

for a in ast.keys():
    sorted_ast = sorted(ast.keys(), key=dist)

    for b in sorted_ast:
        if a != b and is_visible(b, a, ast):
            ast[a].append(b)

counts = {a: len(s) for a,s in ast.items()}

best_ast = max(counts.keys(), key=lambda k: counts[k])
print(best_ast, counts[best_ast])
print(ast[best_ast])

# ********** PART 2 **********

def angle(b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    # first quadrant
    if dx > 0 and dy < 0:
        return -100 + dy/dx
    elif dx > 0 and dy > 0:
        return - dx/dy
    elif dx < 0 and dy > 0:
        return - dx/dy
    elif dx < 0 and dy < 0:
        return 100 + dy/dx
    elif dx == 0 and dy < 0:
        return -200
    elif dy == 0 and dx > 0:
        return -100
    elif dx == 0 and dy > 0:
        return 0
    elif dy == 0 and dx < 0:
        return 100


directions = {}

new_ast = {best_ast: []}

for a in [best_ast]:
    sorted_ast = sorted(ast.keys(), key=dist)
    for b in sorted_ast:
        if b != a and is_visible(b, a, new_ast, directions):
            new_ast[a].append(b)

    sort_keys = sorted(directions.keys(), key=angle)
    dir_lists = []
    for k in sort_keys:
        dir_lists.append(directions[k])

i = 0
count = 0
while count < 200:
    if dir_lists[i]:
        print(dir_lists[i].pop())
        count += 1
        i = (i + 1) % len(dir_lists)
