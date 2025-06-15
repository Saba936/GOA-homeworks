age = int(input("Enter your age"))
time = int(input("enter time: ")) 
while time < 23:
    time = int(input())
if age < 18 and time >= 22:
    print("დროა დაძინების")
elif age >= 60 and time >=21:
    print("დასვენება რეკომენდირებულია")
else:
    print("შეგიძლიათ გააგრძელოთ აქტივობა")