
print(" \n Hi Welcoime to calculator Application!\n" + "\n You choose calculate functions number!")

while True:

    data = input(" 1.COllection\n 2.Reduction\n 3.Multiplication\n 4.Division\n 5.Exit\n :> ")

    try:

        if int(data) == 1:
            C_Firstnumber = input("\n Enter First Numebr:> ")
            C_Secondnumber = input("\n Enter Second Number:> ")
            print("\n Hi, this is the collection:", int(C_Firstnumber) + int(C_Secondnumber), "\n")

        elif int(data) == 2:
            R_Firstnumber = input("\n Enter First Number:> ")
            R_Secondnumber = input("\n Enter Second Number:> ")
            print("\n Hi, This is the Reduction:", int(R_Firstnumber) - int(R_Secondnumber), "\n")

        elif int(data) == 3:
            M_Firstnumber = input("\n Enter First Number:> ")
            M_Secondnumber = input("\n Enter Second Number:> ")
            print("\n Hi, This is the Multiplication:", int(M_Firstnumber) * int(R_Secondnumber), "\n")

        elif int(data) == 4:
            D_Firstnumber = input("\n Enter First Number:> ")
            D_Secondnumber = input("\n Enter Second Number:> ")
            print("\n Hi, This is the Division:", int(D_Firstnumber) / int(D_Secondnumber), "\n")

        elif int(data) == 5:
            break
        
        else:
            print("\n [x] You can nemu numbers but You don't other numbers\n")
    
    except:
        print("\n [x] Hi, You can enter menu number but you don't enter text and textnumber.\n")        
