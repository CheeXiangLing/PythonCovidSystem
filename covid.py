
def viewFile():
    user=[] #Temporarily list to sort data
    user_list=[]
    count=0
    
    with open("userAccount.txt","r")as f:
        lines=f.readlines() # Read everythings from the text file, take note that readlines can't use rstrip 
    
    for line in lines: # TO calculate total number of value in the text file
        count+=1

    with open("userAccount.txt","r")as fa: # Remove the \n from the txt file and adds to the user list
        for x in range(count):
            lines=fa.readline().rstrip("\n") 
            user.append(lines)
        
    total=len(user) #To calculate total value from the txt file
   
    
    numuser=int(total/25) #Calculate total number of user
    user_list = [user[i*25:(i+1)*25] for i in range(numuser)] # Divide the list into sublist, one user will in one list only [[Kelly,1],[Dan,2]], each sublist will contains 25 values
    return user_list

# To obtain the ppv.txt values and put it into a list for easier reference
def viewPPv():
    ppv=[] #Temporarily list to sort data
    ppv_list=[]
    count=0
    
    with open("ppv.txt","r")as f:
        lines=f.readlines() # Read everythings from the text file, take note that readlines can't use rstrip 
    
    for line in lines: # TO calculate total number of value in the text file
        count+=1

    with open("ppv.txt","r")as fa: # Remove the \n from the list and adds it into ppv list
        for x in range(count):
            lines=fa.readline().rstrip("\n") 
            ppv.append(lines)
        
    total=len(ppv) # To calculate total value from the txt file
   
    
    numppv=int(total/5) #Calculate total number of ppv
    ppv_list = [ppv[i*5:(i+1)*5] for i in range(numppv)] # Divide the list into sublist, one ppv will in one list only [[ppv_100,KLCC,2pm,pfizer,""], each ppv will has 5 values
    return ppv_list

  
    

def login():
    user_list = viewFile()
    print(user_list)
    print("--------------Login--------------")
    print("Please fill in login credentials")
    print()
    
    d=bool(True)
    while d:
        id = str(input("Please enter your id:"))
        password = str(input("Please enter your password:"))
        login_successful = False  # flag variable
        for user in user_list:
            if user[1] == id and user[7] == password and user[6]!="admin":
                print("Login successfully")
                login_successful = True
                d = False
                page="user"
                break  # exit the for loop
                

            if user[1] == id and user[7] == password and user[6] == "admin":
                print("Login successfully")
                login_successful = True
                d = False
                page="admin"
                break  # exit the for loop
                

        
        if not login_successful:  # if the for loop ended without finding a match
            print("Login unsuccessfully! Please enter it again!!!")
    
    if(page=="user"):
        user_profile(id,password)
    elif(page=="admin"):
        admin_profile(id,password)
 

def user_profile(id, password):
    user_list = viewFile()

    for user_info in user_list:
        if user_info[1] == id and user_info[7] == password:
            print("\nProfile page")
            print("----------------------------------")
            print("Name:"+user_info[0]+"\nID:"+user_info[1]+"\nAge:"+user_info[2]+"\nPostcode:"+user_info[3]+"\nPhone number:"+user_info[4]+"\nAddress:"+user_info[5]+"\nCategory:"+user_info[6]+"\n")
            print("----------------------------------")
            print("Welcome "+user_info[0]+"!\n")
            print("1. Customize account details ")
            print("2. Update medical history and occupation")
            print("3: Book appointment")
            print("4. Check appointment")
            print("5. Quit")
            option=input_integer("Enter your choice:")
            if(option==1):
                old_value=input(str("Enter the old value(eg: Danny):"))
                if(old_value in user_info): 
                    user_ID=user_info[1] #User id for finding purpose
                    new_value=input(str("Enter the new value:"))
                    with open("userAccount.txt", 'r') as f:    
                        file_lines = f.readlines()
                    found = False
                    for i, line in enumerate(file_lines):
                        if user_ID in line:
                            print(f"Found at line {i}")
                            # Assuming each user's data is stored in 25 lines
                            for j in range(i, i + 25):
                                if j < len(file_lines) and old_value in file_lines[j]:
                                    file_lines[j] = file_lines[j].replace(old_value, new_value)
                                    
                                    if(file_lines[i+1]>"59"):
                                        file_lines[i+5]=file_lines[j].replace(file_lines[j],"Senior\n")
                                    elif(file_lines[i+1]<"13"):
                                        file_lines[i+5]=file_lines[j].replace(file_lines[j],"Children\n")
                                    else:
                                        file_lines[i+5]=file_lines[j].replace(file_lines[j],"Adult\n")
                            found = True
                            break
                    if not found:
                        print(user_ID + " not found in file.")
                    with open("userAccount.txt", 'w') as f:
                        f.writelines(file_lines)
                    print("Update successfully")
                    user_profile(id,password)
            elif(option==2):
                    print("Please answer the question below by typing Yes or No.\nPress enter to continue.")
                    input()
                    print("Are you exhibiting 2 or more symptoms as listed below?")
                    print("-Fever\n-Chills\n-Shivering\n-Body ache\n-Headache\n-Sore throat\n-Nausea or vomiting\n-Diarrhea\n-Fatigue\n-Runny nose or nasal congestion")
                    symptoms = input("Type Yes or No: ")
                    symptoms = symptoms.lower()
                    while(symptoms != 'no' and symptoms != 'yes'):
                        symptoms = input("Please only type Yes or No: ")
                        symptoms = symptoms.lower()

                    print("\nBeside the above,are you exhibiting any of the symptoms listed below?")
                    print("-Cough\n-Difficulty breathing\n-Loss of smell\n-Loss of taste")
                    symptoms2 = input("Type Yes or No: ")
                    symptoms2 = symptoms2.lower()
                    while(symptoms2 != 'no' and symptoms2 != 'yes'):
                        symptoms2 = input("Please only type Yes or No: ")
                        symptoms2 = symptoms2.lower()

                    print("\nHave you attend any event/ areas associated with known COVID-19 cluster?")
                    area = input("Type Yes or No: ")
                    area = area.lower()
                    while(area != 'no' and area != 'yes'):
                        area = input("Please only type Yes or No: ")
                        area = area.lower()

                    print("\nHave you travelled to any country outside Malaysia within 14 days before onset of symptoms?")
                    travelled = input("Type Yes or No: ")
                    travelled = travelled.lower()
                    while(travelled != 'no' and travelled != 'yes'):
                        travelled = input("Please only type Yes or No: ")
                        travelled = travelled.lower()

                    print("\nHave you had close contact to confirmed or suspected case of COVID-19 witin 14 days before onset of illness?")
                    c_contact = input("Type Yes or No: ")
                    c_contact = c_contact.lower()
                    while(c_contact != 'no' and c_contact != 'yes'):
                        c_contact = input("Please only type Yes or No: ")
                        c_contact = c_contact.lower()

                    print("\nAre you under quarantine now?")
                    quarantine = input("Type Yes or No: ")
                    quarantine = quarantine.lower()
                    while(quarantine != 'no' and quarantine != 'yes'):
                        quarantine = input("Please only type Yes or No: ")
                        quarantine = quarantine.lower()
                    
                    print("\nWhat are your occupation?\n1. Medical Personnel\n2. Service industry\n3. Government Functionary\n4. Retiree\n5. Student\n6. Other ")
                    occupation= input_integer("Please select your occupation:")
                   
                    # TO categorize the risk level based on the info that user provided
                    if(occupation==1 or quarantine=="yes"):
                        riskLevel="3: High risk"
                    elif(occupation==2 and symptoms=="yes" and c_contact=="yes"):
                        riskLevel="3: High risk"
                    elif(occupation==3 and symptoms=="yes" and area=="yes" and c_contact=="yes"):
                        riskLevel="1: Low risk"
                    elif(area=="yes" and travelled=="yes" and area=="yes"):
                        riskLevel="2: Medium risk"
                    elif(symptoms=="yes" and symptoms=="yes" and c_contact=="yes"):
                        riskLevel="2: Medium risk"
                    elif(area=="yes" and travelled=="yes" and symptoms2=="yes"):
                        riskLevel="3: High risk"
                    else:
                        riskLevel="1: Low risk"
                    

                    print("Your medical history is successfull updated,press enter to back to menu.")
                    input()

                    # Write into the txt file
                    user_ID=user_info[1]
                    with open("userAccount.txt", 'r') as f:    
                        file_lines = f.readlines()
                    found = False
                    for i, line in enumerate(file_lines):
                        if user_ID in line:
                            print(f"Found at line {i}")
                            # Assuming each user's data is stored in 25 lines
                            file_lines[i+7]=symptoms+"\n"
                            file_lines[i+8]=symptoms2+"\n"
                            file_lines[i+9]=area+"\n"
                            file_lines[i+10]=travelled+"\n"
                            file_lines[i+11]=c_contact+"\n"
                            file_lines[i+12]=quarantine+"\n"
                            file_lines[i+13]=str(occupation)+"\n"
                            file_lines[i+14]=str(riskLevel)+"\n"
                            found = True
                            break
                    if not found:
                        print(user_ID + " not found in file.")
                    with open("userAccount.txt", 'w') as f:
                        f.writelines(file_lines)
                    print("Update successfully")
                    user_profile(id,password)
            elif(option==3):
                print("Book appointment")
                if(user_info[15]=='-'):
                    print("Please first update your medical history and occupation! Thanks")
                    print("Press enter to continue")
                    input()
                    user_profile(id,password)
                else:
                    yesorno = input("Do you want to request an appointment for vaccination? (enter yes or no): ")
                    yesorno = yesorno.lower()
                    if yesorno == "yes":
                        user_ID=user_info[1]
                        with open("userAccount.txt", 'r') as f:    
                            file_lines = f.readlines()
                        found = False
                        for i, line in enumerate(file_lines):
                            if user_ID in line:
                                file_lines[i+15]="want"+"\n"
                                found = True
                                break
                        if not found:
                            print(user_ID + " not found in file.")
                        with open("userAccount.txt", 'w') as f:
                            f.writelines(file_lines)
                        print("Appointment booked successfully! Please wait within three days and check the appointment time.")
                        print("Press enter to continue")
                        input()
                        user_profile(id,password)

                    else:
                        user_profile(id,password)
            
            elif(option==4):
                print("Check your appointment\n")
                if(user_info[17]=='-'):
                    print("Please book appointment first!!!, and wait for admin to assign\n")
                    print("Press enter to continue")
                    input()
                    user_profile(id,password)
                else:
                    print(f"Vaccination id: {user_info[17]}")
                    print(f"Vaccination location: {user_info[18]}")
                    print(f"Vaccination time: {user_info[19]}")
                    print(f"Vaccine type: {user_info[20]}\n")
            
            elif(option==5):
                main_menu()




def admin_profile(id, password):
    print("hi admin")
    user_list = viewFile()
    ppv_list = viewPPv()

    for user_info in user_list:
        if user_info[1] == id and user_info[7] == password:
            print("\nProfile page")
            print("----------------------------------")
            print("Name:"+user_info[0]+"\nID:"+user_info[1]+"\nAge:"+user_info[2]+"\nPostcode:"+user_info[3]+"\nPhone number:"+user_info[4]+"\nAddress:"+user_info[5]+"\nCategory:"+user_info[6]+"\n")
            print("----")
            print("Welcome "+user_info[0]+"!\n")
            print("1. Customize account details")
            print("2. Create appointment time slot:")
            print("3. Assigns time slot")
            print("4. Quit")
            option=input_integer("Please enter your choice:")
            if(option==1):
                old_value=input(str("Enter the old value(eg: Danny):")) # Let the user enter the value that he/she wishs to modify
                if(old_value in user_info): #if the value exists in the list
                    user_ID=user_info[1] #User id for finding purpose
                    new_value=input(str("Enter the new value:"))
                    with open("userAccount.txt", 'r') as f:    
                        file_lines = f.readlines()
                    found = False
                    for i, line in enumerate(file_lines): # Find the position of the old values which allocate at the txt file
                        if user_ID in line:
                            print(f"Found at line {i}") 
                            # Assuming each user's data is stored in 25 lines
                            for j in range(i, i + 25): # To make sure it be added into the user list which will reference to the user id which also means user id must be unique
                                if j < len(file_lines) and old_value in file_lines[j]:
                                    file_lines[j] = file_lines[j].replace(old_value, new_value)
   
                            found = True
                            break
                    if not found:
                        print(user_ID + " not found in file.")
                    with open("userAccount.txt", 'w') as f:
                        f.writelines(file_lines)
                    print("Update successfully")

            elif(option==2):
                
                # To create the time slot for vaccination
                print("Create appointment")
                while True:
                    ppv_id = input("Please enter the ppv id: ")

                    # To identify the ppv id is exists or not from the txt file
                    with open("ppv.txt", 'r+') as file:
                        lines = file.readlines()
                        found = False
                        for line in lines:
                            if ppv_id in line:
                                print("ppv id already exists. Please enter a new one.")
                                found = True
                                break

                        # If the ppv id is not exists
                        if not found:
                            ppv_venue=input("Please enter the venue for vaccination:")
                            ppv_time=input("Please enter the time for vaccination:")
                            ppv_type=input("Please enter the type of vaccine:")

                            file.write(ppv_id+"\n")
                            file.write(ppv_venue+"\n")
                            file.write(ppv_time+"\n")
                            file.write(ppv_type+"\n")
                            file.write("\n")
                            break

                    print("Vaccination added successfully!!!")
                    admin_profile(id,password)

            elif(option==3):
                print("Assign vaccination time slot\n\nUser list")
                
                # Shows the user that have booked their appointment
                for i in range(len(user_list)):
                    if(user_list[i][16]=="want"):
                        for j in range(len(user_info)):
                            
                            print(f"Name: {user_list[i][j]}, User Id: {user_list[i][j+1]}, Age: {user_list[i][j+2]}, Postcode: {user_list[i][j+3]}, Phone number: {user_list[i][j+4]}, Address: {user_list[i][j+5]}, Category: {user_list[i][j+6]}, Risk Level: {user_list[i][j+15]}|")
                            break
                
                # Shows the ppv list
                print("\n PPV list")
                for ppv_info in ppv_list:
                    for i in range(len(ppv_info)):
                        print(f"PPV id: {ppv_info[0]}, PPV location: {ppv_info[1]}, Vacinnation time: {ppv_info[2]}, Vaccine type: {ppv_info[3]}")
                        break
                idd=input("\nPlease enter the user id that you wish to assign the time slot to him/her:")

                with open("userAccount.txt", 'r') as f:
                        file_lines = f.readlines()
               
                found = False
                for i, line in enumerate(file_lines):
                    if idd in line:
                        print(f"ID Found at line {i}")
                        found = True
                        ppv=input("Please enter the ppv id:")
                        for ppv_info in ppv_list:  # Corrected variable name here
                            for j in range(len(ppv_info)):
                                if ppv == ppv_info[j]:
                                    
                                    print("Press enter to continue")
                                    input()
                                    file_lines[i+15]="Assigned\n" # The status which is want will change to Assigned which means it will not appeared in this function
                                    file_lines[i+16]=ppv_info[j]+"\n"
                                    file_lines[i+17]=ppv_info[j+1]+"\n"
                                    file_lines[i+18]=ppv_info[j+2]+"\n"
                                    file_lines[i+19]=ppv_info[j+3]+"\n"
                        break
                        
                with open("userAccount.txt", 'w') as f:
                    f.writelines(file_lines)
                
                admin_profile(id,password)

            elif(option==4):
                main_menu() 


                
                


        

def input_integer(prompt): #To ensure the user enter an integer number
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter only integer number\n")

def signUp():
    print("-----------Sign in------------")
    print("Please fill in the personal informations")
    print()
    name = str(input("Please enter your name:"))
    id = str(input("Please enter your ID:"))
    age = input_integer("Please enter your age:")
    postcode = input_integer("Please enter your postcode:")
    phone = str(input("Please enter your phone number:"))
    address = str(input("Please enter your address:"))
    if(id=="admin0"or id=="admin1" or id=="admin3"): # Admin should only use these id to sign in and then login
        category='admin'
    elif(age>59): # To categorize the age category
        category="Senior"
    elif(age<13):
        category="Junior"
    else:
        category="Adult"
    password=str(input("Please enter your password:"))
    print("Sign in successfully")

    # Add userinfo into the txt file
    file=open("userAccount.txt","a") #Open a file
    file.write(name+"\n") # Write into a file
    file.write(id+"\n")
    file.write(str(age)+"\n") # file.write can only support string instead of other types
    file.write(str(postcode)+"\n")
    file.write(phone+"\n")
    file.write(address+"\n")
    file.write(category+"\n")
    file.write(password+"\n")
    file.write('-'+"\n") # Placeholder for later things such as the vaccination info
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n")
    file.write('-'+"\n\n")

    file.close()



def main_menu():
    print("------------------------------")
    print("^_^ Welcome to Vaccination Assign ^_^")
    print("------------------------------")
    print("1: Login")
    print("2: Sign in")
    print("3: Quit")
    print("------------------------------")
    option=input_integer("Enter your choice:")
    if(option==1):
        login()
        print()
    elif(option==2):
        signUp()
        print()
    elif(option==3):
        print("Thank for using our system")
    elif(option==4):
        viewFile()
    else:
        print("Please enter a valid value")
        print()
        main_menu()



main_menu()
