num1 = int(input())
num2 = int(input())
if num1 > 0 and num2 > 0:
    print("ორივე დადებითია")
elif num1 > 0 and num2 <= 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")
elif num1 <= 0 and num2 > 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")
elif num1 <= 0 and num2 <= 0:
    print("არცერთი არ არის დადებითი")