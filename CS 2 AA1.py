###This program is designed to help the school community keep track of payments inside the cafeteria
students = {
        "mdabadejos": {
            "Password" : "MasterAtDisaster",
            "Balance": 0.00,
            "Transactions": [],
            "Tab Amount": 0.00,
            "Reminders": []
        }
    }
verification = "1234"

def student_system():
    optionstate = ""
    

    
    while True:
        username = input("Enter username to log in:\t")
        if username not in students:
            print("")
            print("Invalid or Unavailble username")
            while True:
                print("")
                print("""Do you want to go to the menu?
0.Yes
1.No

""")
                choice = input("--Enter Choice-- :\t")
                if choice == "0":
                    return
                elif choice == "1":
                    break
                else:
                    print("")
                    print("Invlaid option")
        
        else:
            break

    student = students[username]
    while True:
        password = input(f"Enter password for {username}:\t")
        if password != student["Password"]:
            print("")
            print("Incorrect password")
            while True:
                print("""Do you want to go to the menu?
0.Yes
1.No \n""")
                choice = input("--Enter Choice-- :\t")
                if choice == "0":
                    return
                elif choice == "1":
                    break
                else:
                    print("")
                    print("Invlaid option")
        else:
            break
                
        


    while True:
        print("")
        print("")
        print("")
        print("\nSelect action by number:")
        print("1. Buy Food")
        print("2. Take a Tab/Loan/ Borrow money from canteen")
        print("3. View Status")
        print("4. Log off the Program")
        print("")
        print("")

        optionstate = input("Enter number: ")
        print("")
        print("")

        print("Loading...")

        if optionstate == "1":
            item = input("Enter product:\t")
            quan = int(input("Enter quantity:\t"))
            cost = float(input("Enter price (Php):\t"))
            totcost = quan * cost

            if student["Balance"] >= totcost:
                student["Balance"] -= totcost
                student["Transactions"].append(f"Bought {quan} {item}(s) for ₱{totcost}")
                print("")
                print("Purchase Successful")
                print("")
                print("Balance: ₱", student["Balance"])
            else:
                print("")
                print("Insufficient Purchase cancelled.")


        elif optionstate == "2":
            try:
                loan = float(input("Enter tab/loan amount (Php) (Limit: 200 Php): "))
            except ValueError:
                print("")
                print("Invalid input.")
                continue

            if loan <= 0:
                print("")
                print("Invalid loan amount.")
            elif student["Tab Amount"] + loan > 200:
                print("")
                print("Limit exceeded, transaction cancelled.")
            else:
                print("")
                student["Balance"] += loan
                student["Tab Amount"] += loan
                student["Transactions"].append(f"Loaned ₱{loan}")
                print(f"Borrowed ₱{loan}")
                remaining = 200 - student["Tab Amount"]
                print(f"You can still borrow up to ₱{remaining}")
           

        elif optionstate == "3":
            print("")
            print("")
            print("-------------------- Account Summary --------------------")
            print("")
            print("")

            print("Current Balance:\t", student["Balance"])
            print("")
            print("Borrowed Money:\t", student["Tab Amount"])
            print("")
            print("Transactions:")
            if len(student["Transactions"]) == 0:
                print("No transactions yet")
            else:
                for indx,t in enumerate(student["Transactions"]):
                    print(f"{indx}.  {t}")
            print("")
            print("Reminders:")
            if len(student["Reminders"]) == 0:
                print("No Reminders yet")
            else:
                for indx,r in enumerate(student["Reminders"]):
                    print(f"{indx}.  {r}")

        elif optionstate == "4":
            print("")
            print("Logging off...")
            break
                    
        else:
            print("Invalid input, try again.")

        
            

def staff_menu():
    verification = "1234"

    # 🔐 LOGIN
    while True:
        passwordatp = input("Enter verification key to log in: ")
        if passwordatp != verification:
            print("Incorrect password")
            choice = input("""Go back to menu?
0. Yes
1. Try again
""")
            if choice == "0":
                return
        else:
            break

    # 👤 SELECT STUDENT
    while True:
        username = input("Enter Student Username: ")

        if username in students:
            student = students[username]
        else:
            print("Invalid or Unavailable Username")
            continue

        # 🔁 STAFF ACTION LOOP
        while True:
            print("""
--- STAFF MENU ---


1. View Account
2. Add Reminder
3. Edit Reminder
4. Delete Reminder
5. Change Student
6. Exit

""")

            choice = input("Enter choice:\t")

            # 📖 READ
            if choice == "1":
                print("\n--- Account Summary ---")
                print("")
                print("")
                print("Balance:", student["Balance"])
                print("")
                print("Debt:", student["Tab Amount"])
                print("")

                print("\nTransactions:")
                if not student["Transactions"]:
                    print("No transactions yet")
                else:
                    for i, t in enumerate(student["Transactions"]):
                        print(f"{i}. {t}")
                print("")

                print("\nReminders:")
                if not student["Reminders"]:
                    print("No reminders")
                else:
                    for i, r in enumerate(student["Reminders"]):
                        print(f"{i}. {r}")
            # ➕ CREATE
            elif choice == "2":
                reminder = input("Enter new reminder: ")
                print("")
                student["Reminders"].append(reminder)
                print("Reminder added.")

            # ✏️ UPDATE
            elif choice == "3":
                if not student["Reminders"]:
                    print("No reminders to edit.")
                    continue

                for i, r in enumerate(student["Reminders"]):
                    print(f"{i}. {r}")

                try:
                    index = int(input("Enter reminder number to edit: "))
                    print("")
                    new_text = input("Enter new reminder: ")
                    print("")
                    student["Reminders"][index] = new_text
                    print("Reminder updated.")
                except:
                    print("Invalid selection.")

            # ❌ DELETE
            elif choice == "4":
                print("")
                if not student["Reminders"]:
                    print("No reminders to delete.")
                    continue

                for i, r in enumerate(student["Reminders"]):
                    print(f"{i}. {r}")
                print("")

                try:
                    index = int(input("Enter reminder number to delete:\t"))
                    student["Reminders"].pop(index)
                    print("")
                    print("Reminder deleted.")
                except:
                    print("")
                    print("Invalid selection.")


            elif choice == "5":
                break  

            elif choice == "6":
                return  

            else:
                print("Invalid choice.")

def parent_menu():
    
    verification = "parent1234"

    
    # 🔐 LOGIN
    while True:
        password = input("Enter parent verification key: ")
        if password != verification:
            print("Incorrect password")
            choice = input("""Go back to menu?
0. Yes
1. Try again
""")
            if choice == "0":
                return
            elif choice == "1":
                print("Loading...")
            else:
                print("Invalid Choice")
        else:
            break

    # 👤 SELECT STUDENT
    while True:
        username = input("Enter student's username to log in:\t")
        if username not in students:
            print("")
            print("Invalid or Unavailble username")
            while True:
                print("")
                print("""Do you want to go to the menu?
0.Yes
1.No

""")
                choice = input("--Enter Choice-- :\t")
                if choice == "0":
                    return
                elif choice == "1":
                    break
                else:
                    print("")
                    print("Invlaid option")
        
        else:
            break

    student = students[username]
    while True:
        password = input(f"Enter password for {username}:\t")
        if password != student["Password"]:
            print("")
            print("Incorrect password")
            while True:
                print("""Do you want to go to the menu?
0.Yes
1.No \n""")
                choice = input("--Enter Choice-- :\t")
                if choice == "0":
                    return
                elif choice == "1":
                    break
                else:
                    print("")
                    print("Invlaid option")
        else:
            break
        # 🔁 MENU LOOP
    while True:
        print("""
--- PARENT MENU ---
1. Deposit Money
2. View Student Account
3. Change Student
4. Exit to menu
""")

        choice = input("Enter choice: ")

            # 💰 DEPOSIT
        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Invalid amount.")
                    continue

                    # Auto-pay debt first
                if student["Tab Amount"] > 0:
                    if amount >= student["Tab Amount"]:
                        amount -= student["Tab Amount"]
                        print(f"Debt of ₱{student['Tab Amount']} fully paid.")
                        student["Tab Amount"] = 0
                    else:
                        student["Tab Amount"] -= amount
                        print("Partial debt paid.")
                        amount = 0

                student["Balance"] += amount
                student["Transactions"].append(f"Parent deposited ₱{amount}")
                print("Deposit successful.")

            except ValueError:
                print("Invalid input.")

            # 📊 VIEW
        elif choice == "2":
            print("\n--- Student Account ---")
            print("Balance:", student["Balance"])
            print("Debt:", student["Tab Amount"])

            print("\nTransactions:")
            if not student["Transactions"]:
                print("No transactions")
            else:
                for t in student["Transactions"]:
                    print("-", t)

            print("\nReminders:")
            if not student["Reminders"]:
                print("No reminders")
            else:
                for r in student["Reminders"]:
                    print("-", r)

            
        elif choice == "3":
            break
        elif choice == "4":
            return

        else:
            print("Invalid choice.")


menuchoice = ""

while menuchoice != "1":
    print("""
    0. Login Menu
    1. EXIT
    """)
    print(" ")
    
    menuchoice = input("Enter choice as a number: ")

    if menuchoice == "0":
        print("-== ENTERING LOGIN MENU . . ==-")

        
        while True:
            print("""
0. Student
1. Staff 
2. Parent 
3. EXIT
            """)

            logchoice = input("--Enter Choice-- : ")

            if logchoice == "0":
                print("-== STUDENT MENU ==-")
                print("")
                student_system()
                
            elif logchoice == "1":
                print("-== STAFF MENU ==-")
                print("")
                staff_menu()  
       

            elif logchoice == "2":
                print("-== PARENT MENU ==-")
                print("")
                parent_menu() 


            elif logchoice == "3":
                break
            
            else:
                print("")
                print("Invalid choice.")
