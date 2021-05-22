sets = {'add', 'update', 'intersection', 'difference', 'remove',
        'pop', 'clear', 'discard', 'intersection_update'}
dicts = {'clear', 'keys', 'get', 'items', 'update', 'values'}
a = sets.intersection(dicts)
print(a)