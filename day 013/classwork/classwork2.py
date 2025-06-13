age = int(input("Enter your age"))
if age < 0:
    print("არასწორი ასაკი")
elif age < 13:
    print("ბავშვი")
elif age > 13 and age <= 19:
    print("თინეიჯერი")
elif age > 20 and age <= 59:
    print("ზრდასრული")
else:
    print("პენსიონერი")