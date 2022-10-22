#practice 6

Speed = int(input("Enter the speed : "))
MAxSpeed = int(input("Emter limit Speed : "))
penalty = (((Speed - MAxSpeed)/5) *20)
if Speed < MAxSpeed :
    print("0")
else:
    print(penalty) 
