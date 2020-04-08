import random
A = [[random.randint(0, 10) for i in range(4)],
[random.randint(0, 10) for i in range(4)],
[random.randint(0, 10) for i in range(4)],
[random.randint(0, 10) for i in range(4)]]
print(A)

B=[A[i][i] for i in range(4)]
print(B)