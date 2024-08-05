g = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve,', 'Khendrik', 'Aaron'}
s = sorted(students)
a = (sum(g[0]) / len(g[0]),
     sum(g[1]) / len(g[1]),
     sum(g[2]) / len(g[2]),
     sum(g[3]) / len(g[3]),
     sum(g[4]) / len(g[4]))
students_book = {s[0]: a[0], s[1]: a[1], s[2]: a[2], s[3]: a[3], s[4]: a[4]}
print(students_book)
