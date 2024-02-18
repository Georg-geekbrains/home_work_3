
"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

list_element = [1, 1, 2, 2, 3, 4, 5, 5, 7]

dublicate = set()
unicum = set()
print(dublicate)
print(unicum)
for item in list_element:
    if item in unicum:
        dublicate.add(item)
    else:
        unicum.add(item)

print(list(dublicate))
print(list(unicum))

