score = int(input("enter you score : "))

if score <= 49:
    print("grade : F")
elif score > 49 and score <= 54:
    print("grade : D")
elif score > 54 and score <= 59:
    print("grade : D+")
elif score > 59 and score <= 64:
    print("grade : C")
elif score > 64 and score <= 69:
    print("grade : C+")
elif score > 69 and score <= 74:
    print("grade : B")
elif score > 74 and score <= 79:
    print("grade : B+")
else:
    print("grade : A")