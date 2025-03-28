# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

for _ in range(int(input())):
    n = int(input().strip())
    seq = input().strip()

    s = [0] * n
    zero = [] 
    one = []
    
    for index, char in enumerate(seq):
        new = len(zero) + len(one)
        if char == '0':
            if one:
                new = one.pop()
            zero.append(new)
        else:
            if zero:
                new = zero.pop()
            one.append(new)
        
        s[index] = new

    total = len(zero) + len(one)
    print(total)
    print(" ".join(str(idx + 1) for idx in s))


