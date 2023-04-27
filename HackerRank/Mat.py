if __name__ == '__main__':
    N_s, M_s = (input().split())
    N, M = int(N_s), int(M_s)

    symbol = '.|.'
    ch = 'WELCOME'


half_length = M//2-1
half_width = N//2-1
k = 1

for i in range(half_width+1):
    print(('-' * half_length) + (symbol*k) + ('-' * half_length))
    half_length = half_length - 3
    k = k + 2

middle_length = (M-len(ch))//2
print(('-' * middle_length) + ch + ('-' * middle_length))

half_length = half_length + 3
k = k - 2
for i in range(half_width+1):
    print(('-' * half_length) + (symbol*k) + ('-' * half_length))
    k = k - 2
    half_length = half_length + 3


