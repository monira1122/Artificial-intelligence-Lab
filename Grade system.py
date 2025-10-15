num = int(input("Enter a number: "))
if ((num>0) & (num<100)):
 

 if num >= 80:

    print("A+")
 elif num >= 75:
    print("A")
 elif num >= 70:
    print("A-")
 elif num >= 65:
    print("B+")
 elif num >= 60:
    print("B")
 elif num >= 55:
    print("B-")
 elif num >= 50:
    print("C")
 elif num >= 40:
    print("D")
 else:
    print("F")
else:
   print("invalid")