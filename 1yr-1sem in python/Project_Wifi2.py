
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

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
limit1, limit2, limit3, limit4, limit5 = 0, 0, 0, 0, 0
while num1 < 60:
    print("*", end='')
    num1 += 1
     
print(" \t      \tWifi Router System")


while num2 < 60:
    print("*", end='')
    num2 += 1
    
print("1. PLDT\n2. DITO\n3. CONVERGE\n4. SKY\n5. GLOBE AT HOME")

print("\n* * * * * * * * * *50 to use router!!* * * * * * * * * *\n")

while True:
    cashfromuser1 = int(input("Enter your cash : "))
    if cashfromuser1 >= amount:
        print("\t\t******************")
        print("\t\tReceipt")
        print("\t\tAmount received: ", cashfromuser1)
        print("\t\tChange: ",  cashfromuser1 - amount)
        break
    
    
print("\nEach router have 3 limits")
while True:
    user1 = int(input("Select router: "))
    # start
    if user1 == router1_1:
        while limit1 < 3:
            limit1 = limit1 + 1
            while num3 < 60:
                print("*", end='')
                num3 += 1
            print("\nEach router have 3 limits %d." % limit1)
            router1 = int(input("Enter '505' to connect: "))
            if router1 == 505:
                print("\n\t\tConnected to router 1\n")
            else:
                print("\tWrong passcode")
                limit1 = limit1 - 1
        print("The router 1 is already at limit.")
        while num4 < 60:
            print("*", end='')
            num4 += 1
        while True:
            ask1 = int(input("\nType '1' to change router: "))
            if ask1 == 1:
                break
            # end
    # start
    if user1 == router2_2:
        while limit2 < 3:
            limit2 = limit2 + 1
            while num5 < 60:
                print("*", end='')
                num5 += 1
            print("\nEach router have 3 limits %d." % limit2)
            router2 = int(input("Enter '202' to connect: "))
            if router2 == 202:
                print("\n\t\tConnected to router 2\n")
            else:
                print("\tWrong passcode")
                limit2 = limit2 - 1
        print("The router 2 is already at limit.")
        while num6 < 60:
            print("*", end='')
            num6 += 1
        ask2 = int(input("\nType '1' to change router: "))
        while ask2 == 1:
            break
            # end
    # start
    if user1 == router3_3:
        while limit3 < 3:
            limit3 = limit3 + 1
            while num7 < 60:
                print("*", end='')
                num7 += 1
            print("\nEach router have 3 limits %d." % limit3)
            router3 = int(input("Enter '103' to connect: "))
            if router3 == 103:
                print("\n\t\tConnected to router 1\n")
            else:
                print("\tWrong passcode")
                limit3 = limit3 - 1
        print("The router 3 is already at limit.")
        while num8 < 60:
            print("*", end='')
            num8 += 1
        ask3 = int(input("\nType '1' to change router: "))
        while ask3 == 1:
            break
            # end
    # start
    if user1 == router4_4:
        while limit4 < 3:
            limit4 = limit4 + 1
            while num9 < 60:
                print("*", end='')
                num9 += 1
            print("\nEach router have 3 limits %d." % limit4)
            router4 = int(input("Enter '804' to connect: "))
            if router4 == 804:
                print("\n\t\tConnected to router 1\n")
            else:
                print("\tWrong passcode")
                limit4 = limit4 - 1
        print("The router 4 is already at limit.")
        while num10 < 60:
            print("*", end='')
            num10 += 1
        ask4 = int(input("\nType '1' to change router: "))
        while ask4 == 1:
            break
            # end
    # start
    if user1 == router5_5:
        while limit5 < 3:
            limit5 = limit5 + 1
            while num11 < 60:
                print("*", end='')
                num11 += 1
            print("\nEach router have 3 limits %d." % limit5)
            router5 = int(input("Enter '902' to connect: "))
            if router5 == 902:
                print("\n\t\tConnected to router 1\n")
            else:
                print("\tWrong passcode")
                limit5 = limit5 - 1
        print("The router 5 is already at limit.")
        while num12 < 60:
            print("*", end='')
            num12 += 1
        ask1 = int(input("\nType '1' to change router: "))
        while ask1 == 1:
            break
            # end
    loop1 = int(input("\n \t\tEnter '0' to continue the system and other number to stop the router system: "))
    if loop1 != 0:
        print("Thank you for using our system!!!")
        while num12 < 60:
            print("*", end='')
            num12 += 1
        break

            
