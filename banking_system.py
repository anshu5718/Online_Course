"""
3. Banking System
Q: Menu with options:
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
"""
Menu="""
Choose one of the option:
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
"""
def banking_system():
    var=10000000
    while True:
        print("**********************************")
        print("**********************************")
        print(Menu)
        print("**********************************")
        print("**********************************")
        choice=int(input("Enter your choice: "))
        print("**********************************")
        if choice==1:
            print(var)
            print("**********************************")
        elif choice==2:
            depo=int(input("Enter how much you wanna deposite: "))
            var=var+depo
            print("Your total amount: ",var)
            print("**********************************")
        elif choice==3:
            withdraw=int(input("Enter how much you wanna withdraw: "))
            var=var-withdraw
            print("Your total amount: ",var)
            print("**********************************")
        elif choice==4:
            print("Thanks for visiting")
            break
        else:
            print("Wrong input")
            
            print("**********************************")
banking_system()
