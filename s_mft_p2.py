#practice II
from pickle import FALSE


print(f"WELCOME{chr(3)}")

Num_I = input("Pliz Enter Number : ")
# if Num_I== False :
#     print("YOU MUST USE NUMBER")
# Num_I=Num_I.isdigit()

# Num_I = int(Num_I)

Num_II = input("Pliz Again Enter Number : ")
# if Num_II== False :
#     print("YOU MUST USE NUMBER")
    
# Num_II = int(Num_II)

Num_III = input("Pliz Enter Number : ")
# if Num_I== False :
#     print("YOU MUST USE NUMBER")

#Num_III = int(Num_III)
if (Num_I==False and Num_II==False and Num_III==False ):
    print("YOU MUST ENTER NUMBER")

elif (Num_I < Num_II < Num_III):
    print(Num_I , Num_II , Num_III)
elif (Num_I < Num_III < Num_II):
    print(Num_I , Num_III , Num_II)

elif (Num_II < Num_I < Num_III):
    print(Num_II , Num_I , Num_III)
elif (Num_II < Num_III < Num_I):
    print(Num_II , Num_III , Num_I)

elif (Num_III < Num_II < Num_I):
    print(Num_III , Num_II , Num_I)
elif (Num_III < Num_I < Num_II):
    print(Num_III , Num_I , Num_II)
else :
    print("you should Enter Number (0,1,2,3,...")

#WsalehVII