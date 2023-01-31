
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
num11 = 0
num12 = 0
num13 = 0
num14 = 0
num15 = 0
num16 = 0

router1_1 = 1
router2_2 = 2
router3_3 = 3
router4_4 = 4
router5_5 = 5

router1 = 1
router2 = 2
router3 = 3
router4 = 4
router5 = 5
amount = 50
limit1 = 3
limit2 = 3
limit3 = 3
limit4 = 3
limit5 = 3
while (num1  < 60):
    print("*", end = '')
    num1+=1
     
print(" \t      \tWifi Router System")


while (num2  < 60):
    print("*", end = '')
    num2+=1
    
print("1. PLDT\n2. DITO\n3. CONVERGE\n4. SKY\n5. GLOBE AT HOME")

print("\n* * * * * * * * * *50 to use router!!* * * * * * * * * *\n")

#cashfromuser1 = int(input("Enter your cash : "))
while True:
   cashfromuser1 = int(input("Enter your cash : "))
   if(cashfromuser1 >= amount):
       print("\t\t******************");
       print("\t\tReceipt");
       print("\t\tAmount received: ", cashfromuser1);
       print("\t\tChange: ",  cashfromuser1 - amount)
       break;
    
    
print("\nEach router have 3 limits")


#loop1 = input("Enter '0' to continue the system: ")
while True:
    
    user1 = int(input("Select router: "))
    #start
    if(user1 == router1_1):
            for limit1 in range(1,4):
  
                 while(num3 < 60):
                     print("*",end='')
                     num3+=1
                 print("\nEach router have 3 limits %d." % limit1)   
                 router1 = int(input("Enter '505' to connect: "))
                 if(router1 == 505):
                    
                    print("\n\t\tConnected to router 1\n")
                 else:
                    print("\tInavlid")
                 
            print("The router 1 is already at limit.")
            while(num5 < 60):
                    print("*",end='')
                    num5+=1
            ask1 = int(input("\nType '1' to change router: "))
            while(ask1 == 1):
                 if(ask1 == 1):
                  user1 = int(input("Select router: "))
                  break
    #start
                  
    #end

    #start
    if(user1 == router2_2):
            for limit2 in range(1,4):
                 while(num12 < 60):
                     print("*",end='')
                     num12+=1
                 print("\nEach router have limits %d." % limit2)   
                 router2 = int(input("Enter '202' to connect: "))
                 if(router2 == 202):
                    
                    print("\n\t\tConnected to routet 2\n")
                 else:
                    print("\tInavlid")
            print("The router 2 is already at limit.")
            while(num6 < 60):
                    print("*",end='')
                    num6+=1
            ask2 = int(input("\nType '1' to change router: "))
            while(ask2 == 1):
                 if(ask2 == 1):
                   user1 = int(input("Select router: "))
                   break
                 

    #end
    
     #start
    if(user1 == router3_3):
            for limit3 in range(1,4):
                 while(num8 < 60):
                     print("*",end='')
                     num8+=1
                 printf("\nEach Router have 3 limits %d." % limit3);
                 router3 = int(input("Enter '111' to connect: "))
                 if(router3 == 111):
                    
                    print("\n\t\tConnected to routet 3\n")
                 else:
                    print("\tInavlid")
            print("The router 3 is already at limit.")
            while(num7 < 60):
                    print("*",end='')
                    num7+=1
            ask3 = int(input("\nType '1' to change router: "))
            while(ask3 != 1):
                 if(ask3 == 1):
                   user1 = int(input("Select router: "))
                   break
                 

    #end  
          #start
    if(user1 == router4_4):
            for limit4 in range(1,4):
                 while(num9 < 60):
                     print("*",end='')
                     num9+=1
                 print("\nEach Router have 3 limits %d." % limit4);
                 router4 = int(input("Enter '111' to connect: "))
                 if(router4 == 111):
                    
                    print("\n\t\tConnected to router 4\n")
                 else:
                    print("\tInavlid")
            print("The router 4 is already at limit.")
            while(num10 < 60):
                    print("*",end='')
                    num10+=1
            ask4 = int(input("\nType '1' to change router: "))
            while(ask4 != 1):
                 if(ask4 == 1):
                   user1 = int(input("Select router: "))
                   break
                   
    if(user1 == router5_5):
            for limit5 in range(1,4):
                 while(num13< 60):
                     print("*",end='')
                     num13+=1
                 print("\nEach Router have 3 limits %d." % limit5);
                 router5 = int(input("Enter '902' to connect: "))
                 if(router5 == 902):
                    
                    print("\n\t\tConnected to router 5\n")
                 else:
                    print("\tInavlid")
            print("The router 5 is already at limit.")
            while(num11 < 60):
                    print("*",end='')
                    num11+=1
            ask5 = int(input("\nType '1' to change router: "))
            while(ask5 != 1):
                 if(ask5 == 1):
                   user1 = int(input("Select router: "))
                   break
                 

    #end                
    loop1 = input("\n \t\tEnter '0' to continue the system and other number to stop the router system: ")
    if(loop1 == 0):
        break

            