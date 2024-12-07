while True:
    # Menu
    print("CHECK DIGIT VALIDATOR")
    print("What would you like to validate:")
    print("1. ISBN-10")
    print("2. UPC-12")
    print("Q. Quit Program")
    options = input("Choose an option! =>")

    # UPC
    if options == "2":
        UPC = input("Enter UPC =>")
        a = int(UPC[0])+int(UPC[2])+int(UPC[4])+int(UPC[6])+int(UPC[8])+int(UPC[10])
        b = int(a*3)
        c = int(UPC[1])+int(UPC[3])+int(UPC[5])+int(UPC[7])+int(UPC[9])
        d = int(b)+int(c)
        e = int(d)%10
        f = 10-int(e)
        if int(f) == int(UPC[11]):
            print("Valid!")
        else:
            print("Get out of here you failure and scammer!")

    # ISBN
    elif options == "1":
        ISBN = input("Enter ISBN =>")
        a=(int(ISBN[0])*1) + (int(ISBN[1])*2) + (int(ISBN[2])*3) + (int(ISBN[3])*4)
        b=(int(ISBN[4])*5) + (int(ISBN[5])*6) + (int(ISBN[6])*7) + (int(ISBN[7])*8)
        c=(int(ISBN[8])*9)
        d=int(a) + int(b) + int(c)
        e=int(d)%11
        if int(e) == int(ISBN[9]):
            print("Verified!")
        else:
            print("Get out of here you failure and scammer!")

    # Quit
    elif options == "Q":
        print("Shutting down!")
        break

    # Other Option
    else:
        print("Incorrect option!")
        print("Options: 1,2, and Q")