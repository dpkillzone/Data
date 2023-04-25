import random

# Lav en liste A med 1000 random tal (mellem 0-100)
A = [random.randint(0, 100) for _ in range(1000)]

# Indtast 10 nye værdier til listen
for i in range(10):
    value = int(input("Indtast en ny værdi: "))
    A.append(value)

# Lav en liste B som indeholder værdier mellem [50, 60] fra liste A. De værdier skal fjernes fra liste A.
B = []
for value in A:
    if 50 <= value <= 60:
        B.append(value)
        A.remove(value)

# Sorterer liste A (vha. bubble search)
n = len(A)
for i in range(n):
    for j in range(0, n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

# Udskriv resultater
print("Liste A:", A)
print("Liste B:", B)
