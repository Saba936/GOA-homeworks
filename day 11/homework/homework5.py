A = True
B = False
C = False 
#ა) (A&&!B)||(B&&!A)
#(True and True) or (False and False)რადგან ! ნიშნავს not ცვლის მნიშვნელობას. საბოლოოდ კი იქნება True or False და შემდეგ True.
# პასუხია-True
a = "Answer in ა is: "
result_0 = "True"
#ბ) (B&&C)&&(A||B)
#(False and False) and (True or False), შემდეგ False and True და შემდეგ False.
#პასუხია-False
b = "Answer in ბ is: "
result_1 = "False"
#გ) (A&&!C)||(B&&!A)||(B&&!C)
#(True and True) or (False and False) or (False and True), შემდეგ კი True or False or False, საბოლოოდ კი True.
c = "Answer in გ is: "
result_2 = "True"
#პასუხი-True
print(a + result_0)
print(b + result_1)
print(c + result_2)