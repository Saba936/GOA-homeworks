age = int(input("Enter your age "))
weight = int(input("Enter your weight "))
if age < 10 and weight < 20:
    print("წონა დაბალია")
elif age < 10 and weight>=20 and weight<=40:
    print("წონა ნორმალურია")
elif age < 10 and weight<40:
    print("წონა მაღალია")
elif age>= 10 and age<=17 and weight<40:
    print("წონა დაბალია")
elif age>= 10 and age<=17 and weight>=40 and weight<=65:
    print("წონა ნორმალურია")
elif age>= 10 and age<=17 and weight>65:
    print("წონა მაღალია")
elif age>=18 and weight<50:
    print("წონა დაბალია")
elif age>=18 and weight>=50 and weight<=90:
    print("წონა ნორმალურია")
elif age>=18 and weight>90:
    print("წონა მაღალია")