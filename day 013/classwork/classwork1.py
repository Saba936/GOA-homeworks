heart_rate = int(input("Enter your heart rate:"))
if heart_rate > 180:
    print("მაღალია")
elif heart_rate > 160 and heart_rate < 170:
    print("ნორმალურია")
else:
    print("დაბალია")