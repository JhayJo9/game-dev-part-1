router1_1 = 1
num3, num4 = 0, 0
limit1 = 0
user1 = int(input("Select router: "))
if user1 == router1_1:
    while limit1 < 3:
        limit1 = limit1 + 1
        router1 = int(input("Enter '505' to connect: "))
        if router1 == 505:
            print("\n\t\tConnected to router 1\n")
        else:
            limit1 = limit1 - 1
            print("\tInvalid")
    print("The router 1 is already at limit.")
    while num4 < 60:
        print("*", end='')
        num4 += 1
    ask1 = int(input("\nType '1' to change router: "))
    while ask1 == 1:
        break
while num3 < 60:
    print("*", end='')
    num3 += 1
