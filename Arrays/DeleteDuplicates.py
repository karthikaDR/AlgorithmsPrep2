a = [1,1,2,3,3,4,5,5]


write = 1

for i in range(1, len(a)):

    if (a[write - 1]) != a[i]:
        a[write] = a[i]
        write += 1
print(a[:write], write)