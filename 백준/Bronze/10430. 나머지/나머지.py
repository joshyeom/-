a = input()
A, B, C = list(map(int, a.split()))

print((A+B)%C)
print(((A%C) + (B%C))%C)
print( (A*B)%C)
print(((A%C) * (B%C))%C)
