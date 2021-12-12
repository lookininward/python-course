simple_list = [1, 2, 3, 4, 5]
simple_list.extend([5, 6, 7])

del(simple_list[0])
print(simple_list)

d = {
    "name": "Max"
}

del(d["name"])
print(d.items())

t = (1, 2, 3)
# del(t[0])
print(t.index(1))

s = {"Max", "Anna", "Max"}
s.discard("Anna")
print(s)
