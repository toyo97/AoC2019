from functools import reduce

def compute_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + compute_fuel(fuel)


with open('1.in', 'r') as f:
    values = list(map(int, f.read().strip().split('\n')))

sum = reduce(lambda a,b: a+compute_fuel(b), values, 0)
print(sum)
