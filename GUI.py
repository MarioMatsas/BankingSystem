# Imports
from tkinter import *
from PIL import ImageTk, Image 
import os
import json
from random import randrange
from datetime import datetime

#Feching the information from the file with the bank accounts, or creating a new file to store them into. 
try:
    with open("registered_accounts.json") as f:
        bank_accounts = json.load(f)
except FileNotFoundError:
    bank_accounts = []

#Main window
master = Tk()
master.title("MM Banking™")

#Image Import
img = Image.open("MM logo.jpg")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

#Functions
def fin_register():
    #Variables
    full_name = temp_full_name.get()
    father_name = temp_father_name.get()
    mother_name = temp_mother_name.get()
    date_of_birth = temp_date_of_birth.get()
    phone_number = temp_phone_number.get()
    email = temp_email.get()

    #Generating random values for credit card, cvv, exp. month and year
    credit_card = str(randrange(1000000000000000, 10000000000000000))
    cvv = str(randrange(100, 1000))
    expiration_month = str(str(randrange(1, 13)).zfill(2))
    expiration_year = str(int(datetime.now().year) + 6)

    if full_name=="" or father_name=="" or mother_name=="" or date_of_birth=="" or phone_number=="" or email=="":
        notif1.config(fg="Red", text="All fields required *")
        return
    else:
        bank_accounts.append({
            "Full name": full_name.upper(),
            "Father full name": father_name.upper(),
            "Mother full name": mother_name.upper(),
            "Date of birth": date_of_birth,
            "Phone number": phone_number,
            "E-mail address": email,
            "Credit_card": credit_card,
            "CVV": cvv,
            "Expiration Date": expiration_month + '/' + expiration_year,
            "Account balance": 0
        })

        with open("registered_accounts.json", "w") as f:
            json.dump(bank_accounts, f)

        #Registration Complete Window
        completion_window = Toplevel(master)
        completion_window.title("Registration Complete")

        #Labels
        Label(completion_window, text="Your account has been successfully registered!", font=("Arial", 12)).grid(row=0, sticky=N, pady=10)
        Label(completion_window, text="Next you will find a copy of you account's details", font=("Arial", 12)).grid(row=0, column=1, sticky=N, pady=10)
        Label(completion_window, text="Full name:", font=("Arial", 12)).grid(row=1, sticky=W, pady=1)
        Label(completion_window, text="Father's full name:", font=("Arial", 12)).grid(row=2, sticky=W, pady=1)
        Label(completion_window, text="Mother's full name:", font=("Arial", 12)).grid(row=3, sticky=W, pady=1)
        Label(completion_window, text="Date of birth:", font=("Arial", 12)).grid(row=4, sticky=W, pady=1)
        Label(completion_window, text="Phone number:", font=("Arial", 12)).grid(row=5, sticky=W, pady=1)
        Label(completion_window, text="E-mail address:", font=("Arial", 12)).grid(row=6, sticky=W, pady=1)
        Label(completion_window, text="Credit_card:", font=("Arial", 12)).grid(row=7, sticky=W, pady=1)
        Label(completion_window, text="CVV:", font=("Arial", 12)).grid(row=8, sticky=W, pady=1)
        Label(completion_window, text="Expiration Date:", font=("Arial", 12)).grid(row=9, sticky=W, pady=1)
        Label(completion_window, text="Account balance:", font=("Arial", 12)).grid(row=10, sticky=W, pady=1)
        Label(completion_window, text=f"{full_name}", font=("Arial", 12)).grid(row=1, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{father_name}", font=("Arial", 12)).grid(row=2, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{mother_name}", font=("Arial", 12)).grid(row=3, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{date_of_birth}", font=("Arial", 12)).grid(row=4, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{phone_number}", font=("Arial", 12)).grid(row=5, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{email}", font=("Arial", 12)).grid(row=6, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{credit_card}", font=("Arial", 12)).grid(row=7, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{cvv}", font=("Arial", 12)).grid(row=8, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{expiration_month}/{expiration_year}", font=("Arial", 12)).grid(row=9, column=1, sticky=W, pady=1)
        Label(completion_window, text=f"{0} €", font=("Arial", 12)).grid(row=10, column=1, sticky=W, pady=1)
        Label(completion_window, text="Thank you for choosing our services.", font=("Arial", 8)).grid(row=11, column=1, sticky=E, pady=1)


def register():
    #Varieables
    global temp_full_name
    global temp_father_name
    global temp_mother_name
    global temp_date_of_birth
    global temp_phone_number
    global temp_email
    global notif1

    temp_full_name=StringVar()
    temp_father_name=StringVar()
    temp_mother_name=StringVar()
    temp_date_of_birth=StringVar()
    temp_phone_number=StringVar()
    temp_email=StringVar()

    #Register Window
    register_screen = Toplevel(master)
    register_screen.title("Register Account")

    #Register Labels
    Label(register_screen, text="To register a new account,", font=("Arial", 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="please fill the form below", font=("Arial", 12)).grid(row=0, column=1, pady=10)
    Label(register_screen, text="Full Name", font=("Arial", 12)).grid(row=1, sticky=W,pady=1)
    Label(register_screen, text="Father's full name", font=("Arial", 12)).grid(row=2, sticky=W,pady=1)
    Label(register_screen, text="Mother's full name", font=("Arial", 12)).grid(row=3, sticky=W,pady=1)
    Label(register_screen, text="Date of birth", font=("Arial", 12)).grid(row=4, sticky=W,pady=1)
    Label(register_screen, text="Phone number", font=("Arial", 12)).grid(row=5, sticky=W,pady=1)
    Label(register_screen, text="E-mail address", font=("Arial", 12)).grid(row=6, sticky=W,pady=1)
    notif1 = Label(register_screen, font=("Arial", 10))
    notif1.grid(row=8, column=1, sticky=E, pady=3)
    

    #Register Entries
    Entry(register_screen, width=20, textvariable=temp_full_name).grid(row=1, column=1, pady=1, padx=5)
    Entry(register_screen, width=20, textvariable=temp_father_name).grid(row=2, column=1, pady=1, padx=5)
    Entry(register_screen, width=20, textvariable=temp_mother_name).grid(row=3, column=1, pady=1, padx=5)
    Entry(register_screen, width=20, textvariable=temp_date_of_birth).grid(row=4, column=1, pady=1, padx=5)
    Entry(register_screen, width=20, textvariable=temp_phone_number).grid(row=5, column=1, pady=1, padx=5)
    Entry(register_screen, width=20, textvariable=temp_email).grid(row=6, column=1, pady=1, padx=5)

    #Register Button
    Button(register_screen, text="Register", font=("Arial", 12), command=fin_register).grid(row=7, sticky=E, pady=10)


def fin_deposit():
    if temp_deposit_money.get() == "":
        notif3.config(fg="Red", text="Deposit amount not found *")
        return
        
    diposit_money = float(temp_deposit_money.get())   
    bank_accounts[k]["Account balance"] += diposit_money
    with open("registered_accounts.json", "w") as f:
        json.dump(bank_accounts, f)
    notif3.config(fg="Green", text="The amount has been deposited!")

    Label(login_menu, text=f"User: {bank_accounts[k]['Full name']}\nAccount Balance: {bank_accounts[k]['Account balance']}", font=("Arial", 15)).grid(row=0, sticky=N, pady=10, padx=10)
    return


def deposit():
    #Variables
    global temp_deposit_money
    global notif3
    temp_deposit_money = StringVar()

    #Deposit Window
    deposit_window = Toplevel(master)
    deposit_window.title = "Deposit Window"

    #Labels
    Label(deposit_window, text="Enter the amount you would like to deposit", font=("Arial", 12)).grid(row=0, sticky=N, pady=10, padx=10)
    notif3 = Label(deposit_window, font=("Arial", 8))
    notif3.grid(row=4, sticky=E, pady=3)

    #Buttons
    Button(deposit_window, text="Deposit", font=("Arial", 12), command=fin_deposit).grid(row=3, sticky=N, pady=5)

    #Entries
    Entry(deposit_window, width=20, textvariable=temp_deposit_money).grid(row=1, sticky=N, pady=5)

def fin_withdrawal():
    if temp_withdraw_money.get() == "":
        notif4.config(fg="Red", text="Withdrawal amount not found *")
        return
        
    withdraw_money = float(temp_withdraw_money.get())   
    if bank_accounts[k]["Account balance"] < withdraw_money:
        notif4.config(fg="Red", text="Your account balance is less than the withdrawal *")
    else:
        bank_accounts[k]["Account balance"] -= withdraw_money
        with open("registered_accounts.json", "w") as f:
            json.dump(bank_accounts, f)
        notif4.config(fg="Green", text="The amount has been withrawed!")

        Label(login_menu, text=f"User: {bank_accounts[k]['Full name']}\nAccount Balance: {bank_accounts[k]['Account balance']}", font=("Arial", 15)).grid(row=0, sticky=N, pady=10, padx=10)
        return
    

def withdrawal():
    #Variables
    global temp_withdraw_money
    global notif4
    temp_withdraw_money = StringVar()

    #Withdrawal Window
    withdrawal_window = Toplevel(master)
    withdrawal_window.title = "Withdrawal Window"

    #Labels
    Label(withdrawal_window, text="Enter the amount you would like to withdraw", font=("Arial", 12)).grid(row=0, sticky=N, pady=10, padx=10)
    notif4 = Label(withdrawal_window, font=("Arial", 10))
    notif4.grid(row=4, sticky=E, pady=3)

    #Buttons
    Button(withdrawal_window, text="Withdraw", font=("Arial", 12), command=fin_withdrawal).grid(row=3, sticky=N, pady=5)

    #Entries
    Entry(withdrawal_window, width=20, textvariable=temp_withdraw_money).grid(row=1, sticky=N, pady=5)

def acc_details():
    #Account Details Window
    acc_details_window = Toplevel(master)
    acc_details_window.title = "Account Details"

    #Labels
    Label(acc_details_window, text=f"Full name:", font=("Arial", 12)).grid(row=0, sticky=W, pady=1)
    Label(acc_details_window, text=f"Father's full name:", font=("Arial", 12)).grid(row=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"Mother's full name:", font=("Arial", 12)).grid(row=2, sticky=W, pady=1)
    Label(acc_details_window, text=f"Date of birth:", font=("Arial", 12)).grid(row=3, sticky=W, pady=1)
    Label(acc_details_window, text=f"Phone number:", font=("Arial", 12)).grid(row=4, sticky=W, pady=1)
    Label(acc_details_window, text=f"E-mail address:", font=("Arial", 12)).grid(row=5, sticky=W, pady=1)
    Label(acc_details_window, text=f"Credit_card:", font=("Arial", 12)).grid(row=6, sticky=W, pady=1)
    Label(acc_details_window, text=f"CVV:", font=("Arial", 12)).grid(row=7, sticky=W, pady=1)
    Label(acc_details_window, text=f"Expiration Date:", font=("Arial", 12)).grid(row=8, sticky=W, pady=1)
    Label(acc_details_window, text=f"Account balance:", font=("Arial", 12)).grid(row=9, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Full name']}", font=("Arial", 12)).grid(row=0, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Father full name']}", font=("Arial", 12)).grid(row=1, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Mother full name']}", font=("Arial", 12)).grid(row=2, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Date of birth']}", font=("Arial", 12)).grid(row=3, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Phone number']}", font=("Arial", 12)).grid(row=4, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['E-mail address']}", font=("Arial", 12)).grid(row=5, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Credit_card']}", font=("Arial", 12)).grid(row=6, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['CVV']}", font=("Arial", 12)).grid(row=7, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Expiration Date']}", font=("Arial", 12)).grid(row=8, column=1, sticky=W, pady=1)
    Label(acc_details_window, text=f"{bank_accounts[k]['Account balance']} €", font=("Arial", 12)).grid(row=9, column=1, sticky=W, pady=1)

def fin_modify_account():
    #Variables
    full_name2 = temp_full_name2.get()
    father_name2 = temp_father_name2.get()
    mother_name2 = temp_mother_name2.get()
    date_of_birth2 = temp_date_of_birth2.get()
    phone_number2 = temp_phone_number2.get()
    email2 = temp_email2.get()

    if full_name2=="" or father_name2=="" or mother_name2=="" or date_of_birth2=="" or phone_number2=="" or email2=="":
        notif6.config(fg="Red", text="All fields required *")
        return

    bank_accounts[k]["Full name"] = full_name2.upper()
    bank_accounts[k]["Father full name"] = father_name2.upper()
    bank_accounts[k]["Mother full name"] = mother_name2.upper()
    bank_accounts[k]["Date of birth"] = date_of_birth2
    bank_accounts[k]["Phone number"] = phone_number2
    bank_accounts[k]["E-mail address"] = email2               
                    
    with open("registered_accounts.json", "w") as f:
        json.dump(bank_accounts, f)

    #Registration Complete Window
    mod_window = Toplevel(master)
    mod_window.title("Modification Complete")

    #Labels
    Label(mod_window, text="Your account details have been successfully changed!", font=("Arial", 12)).grid(row=0, sticky=N, pady=10)
    Label(mod_window, text="Next you will find a copy of you account's details", font=("Arial", 12)).grid(row=0, column=1, sticky=N, pady=10)
    Label(mod_window, text="Full name:", font=("Arial", 12)).grid(row=1, sticky=W, pady=1)
    Label(mod_window, text="Father's full name:", font=("Arial", 12)).grid(row=2, sticky=W, pady=1)
    Label(mod_window, text="Mother's full name:", font=("Arial", 12)).grid(row=3, sticky=W, pady=1)
    Label(mod_window, text="Date of birth:", font=("Arial", 12)).grid(row=4, sticky=W, pady=1)
    Label(mod_window, text="Phone number:", font=("Arial", 12)).grid(row=5, sticky=W, pady=1)
    Label(mod_window, text="E-mail address:", font=("Arial", 12)).grid(row=6, sticky=W, pady=1)
    Label(mod_window, text="Credit_card:", font=("Arial", 12)).grid(row=7, sticky=W, pady=1)
    Label(mod_window, text="CVV:", font=("Arial", 12)).grid(row=8, sticky=W, pady=1)
    Label(mod_window, text="Expiration Date:", font=("Arial", 12)).grid(row=9, sticky=W, pady=1)
    Label(mod_window, text="Account balance:", font=("Arial", 12)).grid(row=10, sticky=W, pady=1)
    Label(mod_window, text=f"{full_name2}", font=("Arial", 12)).grid(row=1, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{father_name2}", font=("Arial", 12)).grid(row=2, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{mother_name2}", font=("Arial", 12)).grid(row=3, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{date_of_birth2}", font=("Arial", 12)).grid(row=4, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{phone_number2}", font=("Arial", 12)).grid(row=5, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{email2}", font=("Arial", 12)).grid(row=6, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{bank_accounts[k]['Credit_card']}", font=("Arial", 12)).grid(row=7, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{bank_accounts[k]['CVV']}", font=("Arial", 12)).grid(row=8, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{bank_accounts[k]['Expiration Date']}", font=("Arial", 12)).grid(row=9, column=1, sticky=W, pady=1)
    Label(mod_window, text=f"{bank_accounts[k]['Account balance']} €", font=("Arial", 12)).grid(row=10, column=1, sticky=W, pady=1)
    Label(mod_window, text="Thank you for choosing our services.", font=("Arial", 8)).grid(row=11, column=1, sticky=E, pady=1)
    Label(login_menu, text=f"User: {bank_accounts[k]['Full name']}\nAccount Balance: {bank_accounts[k]['Account balance']}", font=("Arial", 15)).grid(row=0, sticky=N, pady=10, padx=10)
    return

def modify_account():
    #Varieables
    global temp_full_name2
    global temp_father_name2
    global temp_mother_name2
    global temp_date_of_birth2
    global temp_phone_number2
    global temp_email2
    global notif6

    temp_full_name2=StringVar()
    temp_father_name2=StringVar()
    temp_mother_name2=StringVar()
    temp_date_of_birth2=StringVar()
    temp_phone_number2=StringVar()
    temp_email2=StringVar()

    #Account Modification Window
    mod_acc_window = Toplevel(master)
    mod_acc_window.title = "Modification Window"

    #Labels
    Label(mod_acc_window, text="Feel free to modify", font=("Arial, 12")).grid(row=0, sticky=N, pady=10)
    Label(mod_acc_window, text="any information you want.", font=("Arial, 12")).grid(row=0, column=1, sticky=N, pady=10)
    Label(mod_acc_window, text="Full name:", font=("Arial", 12)).grid(row=1, sticky=W, pady=1)
    Label(mod_acc_window, text="Father's full name:", font=("Arial", 12)).grid(row=2, sticky=W, pady=1)
    Label(mod_acc_window, text="Mother's full name:", font=("Arial", 12)).grid(row=3, sticky=W, pady=1)
    Label(mod_acc_window, text="Date of birth:", font=("Arial", 12)).grid(row=4, sticky=W, pady=1)
    Label(mod_acc_window, text="Phone number:", font=("Arial", 12)).grid(row=5, sticky=W, pady=1)
    Label(mod_acc_window, text="E-mail address:", font=("Arial", 12)).grid(row=6, sticky=W, pady=1)
    notif6 = Label(mod_acc_window, font=("Arial", 10))
    notif6.grid(row=7, column=1, sticky=E, pady=3)

    #Entries
    Entry(mod_acc_window, width=20, textvariable=temp_full_name2).grid(row=1, column=1, pady=1, padx=5)
    Entry(mod_acc_window, width=20, textvariable=temp_father_name2).grid(row=2, column=1, pady=1, padx=5)
    Entry(mod_acc_window, width=20, textvariable=temp_mother_name2).grid(row=3, column=1, pady=1, padx=5)
    Entry(mod_acc_window, width=20, textvariable=temp_date_of_birth2).grid(row=4, column=1, pady=1, padx=5)
    Entry(mod_acc_window, width=20, textvariable=temp_phone_number2).grid(row=5, column=1, pady=1, padx=5)
    Entry(mod_acc_window, width=20, textvariable=temp_email2).grid(row=6, column=1, pady=1, padx=5)

    #Buttons
    Button(mod_acc_window, text="Apply Changes", font=("Arial", 12), command=fin_modify_account).grid(row=7, sticky=E, pady=10)



def login_check():
    #Login Check Variable
    credit_card = temp_credit_card.get()
    cvv = temp_cvv.get()
    correct_details = 0
    global k

    for i in range(len(bank_accounts)):
        if bank_accounts[i]["Credit_card"] == credit_card and bank_accounts[i]["CVV"] == cvv:
            correct_details += 1
            k = i
        else:
            continue
    
    if correct_details == 0:
        notif2.config(fg="Red", text="Incorrect details *") 
    else:
        #Login Menu Window
        global login_menu
        login_menu = Toplevel(master)
        login_menu.title("Login Menu")

        #Labels
        Label(login_menu, text=f"User: {bank_accounts[k]['Full name']}\nAccount Balance: {bank_accounts[k]['Account balance']}", font=("Arial", 15)).grid(row=0, sticky=N, pady=10, padx=10)
        
        #Buttons 
        Button(login_menu, width=16, text="Make A Deposit", font=("Arial",12), command=deposit).grid(row=2, sticky=N, pady=3, padx=10)
        Button(login_menu, width=16, text="Make A Withdrawal", font=("Arial",12), command=withdrawal).grid(row=3, sticky=N, pady=3, padx=10)
        Button(login_menu, width=16, text="Account Details", font=("Arial",12), command=acc_details).grid(row=4, sticky=N, pady=3, padx=10)
        Button(login_menu, width=16, text="Modify Details", font=("Arial",12), command=modify_account).grid(row=5, sticky=N, pady=3, padx=10)


        

def login():
    #Login Variables
    global temp_credit_card
    global temp_cvv
    global notif2
    temp_credit_card = StringVar()
    temp_cvv = StringVar()
    

    #Login Window
    login_window = Toplevel(master)
    login_window.title("Login Screen")

    #Login Labels
    Label(login_window, text="Credit Card Number:", font=("Arial", 12)).grid(row=0, sticky=W, pady=5, padx=5)
    Label(login_window, text="CVV:", font=("Arial", 12)).grid(row=1, sticky=W, pady=5, padx=5)
    notif2 = Label(login_window, font=("Arial", 10))
    notif2.grid(row=2, column=1, sticky=E, pady=10)

    #Login Entries
    Entry(login_window, width=20, textvariable=temp_credit_card).grid(row=0, column=1, pady=5, padx=5)
    Entry(login_window, width=20, textvariable=temp_cvv).grid(row=1, column=1, pady=5, padx=5)

    #Login Buttons
    Button(login_window, text="Login", font=("Arial", 12), command=login_check).grid(row=2, sticky=E, pady=5)


#Labels
Label(master, text="MM Banking Service", font=("Arial", 15)).grid(row=0, sticky=N, pady=10)
Label(master, text="For the people. By the people", font=("Arial", 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=20)

#Buttons
Button(master, text="Register", font=("Arial", 12), width=20, command=register).grid(row=3, sticky=N, pady=3)
Button(master, text="Login", font=("Arial", 12), width=20, command=login).grid(row=4, sticky=N, pady=5)


master.mainloop()
