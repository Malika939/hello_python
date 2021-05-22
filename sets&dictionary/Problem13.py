farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = set()
a = farm_2.difference(farm_1)
farm_3.update(a)
print(farm_3)