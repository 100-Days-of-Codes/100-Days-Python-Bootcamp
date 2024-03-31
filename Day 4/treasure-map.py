row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

x, y = input("Where do yo want to put the treasure? enter coloum row: ").split(" ")

map[int(y) - 1][int(x) - 1] = "⬛"

print(row1)
print(row2)
print(row3)