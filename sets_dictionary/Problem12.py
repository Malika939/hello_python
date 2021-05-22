c = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
l = set()
e = c.intersection(b)
l.update(e)
print(l)