username=input("Username:")
Password=input("Password:")
if username=="kan" and Password=="123":
    print("Hello Stranger,What are you buying???")
    print("1.Tiny Gun:5000THB")
    print("2.Also a Gun but a lot longer:500000THB")
    select=int(input("which one do you want:"))
    quantity=int(input("How many gun do you want:"))
    if select==1:
        print(f"Total price is{5000*quantity} TTHB")
    elif select==2:
        print(f"Total price is{500000*quantity} TTHB")
else:
    print("Unknow user")