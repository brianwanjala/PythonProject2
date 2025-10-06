def topten(n):
    n=1
    while n <= 10:
        sq=n*n
        yield sq
        n+=1
values = topten(10)

for i in values:
    print(i, end='')
    print()