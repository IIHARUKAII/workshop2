start = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
end = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
index = 2

for first in start:
    print("\t", index, "\n")
    for last in end:
        print(first, "*", last, "=", first * last)
    print("----------------")
    index += 1
