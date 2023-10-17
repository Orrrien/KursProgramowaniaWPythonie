import random
l = []
for i in range(100):
    l.append(random.randrange(1, 100))
for i in range(100):
    print(l[i])
print("\n")
for i in range(99, -1, -1):
    print(l[i])