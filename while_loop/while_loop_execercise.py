start = 2
while start <= 12:
    print("\t", [start], "\n")
    end = 1
    while end <= 12:
        print(start, "*", end, "=", start * end, "\n")
        end += 1
    print("--------------------")
    start += 1