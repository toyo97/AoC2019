seq = list(map(int, open('test16_1.in').read().strip()))

base = [0, 1, 0, -1]

n_phases = 100
#seq_length = len(seq)
#
#for p in range(n_phases):
##    print(f'Phase: {p}')
#    out = []
#    print(seq)
#    for it in range(1, seq_length+1):
#        res = 0
#        for i in range(seq_length):
#            j = ((i+1) // it) % 4
##            print(base[j], end=' ')
#            res += seq[i] * base[j]
#        # append only the last digit
##        print('\n')
#        out.append(int(str(res)[-1]))
#    seq = out[:]
#
#
#print(''.join(map(str,seq))[:8])


# ***** PART 2 *****

M = 10
seq_len = len(seq) * M

n_it = 7
for it in range(n_it):
    for i in range(seq_len):
        count = 0
        j = ((i+1) // it) % 4
        i = i % len(seq)
        if base[j] != 0:
            count += 1
#            print(f'{seq[i] * base[j]}', end='+')
