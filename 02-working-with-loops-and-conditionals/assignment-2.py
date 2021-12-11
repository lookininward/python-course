names = ["Michael", "Kiersty", "Misty", "Dee", "Natlaie"]

for name in names:
    if len(name) > 5 and ("n" in name or "N" in name):
        print(name)
        print('has n or N')


while len(names) >= 1:
    names.pop()


print(names)
