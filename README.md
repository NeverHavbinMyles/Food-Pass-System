# Food-Pass-System
#Canteen Card System

##Description:
Food-Pass-System (F.P.S.) is a Python-based application designed to improve canteen transactions by making them faster, more organized, and cashless.

The system helps:

Students manage their food budget
Parents monitor and fund student accounts
Canteen staff manage reminders and account information

The application uses a role-based system where each user type has specific functions and permissions.


##Features:
Student Functions:
Purchase food items,
View account balance,
View transaction history,
Borrow money through a limited tab/loan system,
View reminders from canteen staff

Parent Functions:
Deposit money into student accounts,
Pay existing student debt/tab,
Monitor balances and transactions,
View reminders and account status

Staff Functions:
Access student account summaries,
Manage reminders using CRUD operations:
(Create reminders,
Read reminders,
Update reminders,
Delete reminders)

##Database Structure:
students = {
    "username": {
        "Name": "",
        "Balance": 0.00,
        "Transactions": [],
        "Tab Amount": 0.00,
        "Reminders": []
    }
}


##Installation Requirements:
Python
Git (Optional)

##Installation Instructions:
1.Clone the Repository (git clone https://github.com/NeverHavbinMyles/Food-Pass-System.git)
2. Open Project Folder (cd Food-Pass-System)
3. Run the program (python main.py / python3 main.py)



##Project Status: Under Development
The project is currently functional as a prototype and continues to improve through:

Feature additions,
System optimization,
Code restructuring,
User interface improvements

Future Improvements:
Application support,
QR code integration,
Database integration (SQLite),
Generating menu,
Notification System,
Online Payment System,
Improved Authentication and Security,






Developed by:
NeverHavbinMyles
School Project-- Smart Canteen Management Prototype
