#practice 4
Num =input("Pliz Enter Number : ")
Num =Num.isdigit()
Num=int(Num)
if Num==False:
  print("pliz Enter Number")
  if Num!= False:
    Num=int(Num)
elif Num %2 == 0:
  print("odd")
elif Num %2 == 1:
  print("even")
else:
  print("*")


print(type(Num))
