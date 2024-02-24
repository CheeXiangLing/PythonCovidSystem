def login():
    print("Login")

def signUp():
    print("SignUp")

def main_menu():
    print("------------------------------")
    print("^_^ Welcome to Vaccination Assign ^_^")
    print("------------------------------")
    print("1: Login")
    print("2: Sign in")
    print("3: Quit")
    print("------------------------------")
    while(True):
        try:
            option=int(input("Enter your choice:"))
            if(option==1):
                login()
                print()
                break
            elif(option==2):
                signUp()
                print()
                break
            elif(option==3):
                print("Thank for using our system")
                break
            else:
                print("Please enter a valid value")
                print()
        except ValueError:
            print("Please enter an integer number")
            print()


main_menu()
