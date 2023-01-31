num1 = 0
num2 = 0
num3 = 0
num4 = 0
router1_1 = 1
amount = 50
limit1 = 3
while (num1  < 60):
    print("*", end = '')
    num1+=1
     
print(" \t      \tWifi Router System")


while (num2  < 60):
    print("*", end = '')
    num2+=1
    
print("1. PLDT\n2. DITO\n3. CONVERGE\n4. SKY\n5. GLOBE AT HOME")

#cashfromuser1 = int(input("Enter your cash : "))
while True:
   cashfromuser1 = int(input("Enter your cash : "))
   if(cashfromuser1 >= amount):
       
       print("Your change is ",  cashfromuser1 - amount)
       break;
    
    
print("Each router have 3 limits")

while True:
    user1 = int(input("Select router: "))
    if(user1 == router1_1):
        while True: 
            while(limit1 > 0):
                 
                 
                 while(num3 < 60):
                     print("*",end='')
                     num3+=1
                 router1 = int(input("Enter '505' to connect: "))
                 if(router1 == 505):
                    
                    print("\tConnected")
                 else:
                       
                    print("\tInavlid")
                    limit1-=1
                        
        print("The router 1 is already at limit.\n")
                 
                 while(num4 < 60):
                       print("*",end='')
                       num4+=1