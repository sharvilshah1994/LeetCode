a = [10, 10]

for _ in range(len(a) + 1):
    if sum(a[0:_]) == sum(a[_: len(a)]):
        print("Balanced")
