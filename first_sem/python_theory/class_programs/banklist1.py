bank_details2 = []
number = int(input("Enter how many accounts do you need? "))

for n in range(number):
    acc_name = input("Enter Account Name: ")
    acc_no = input("Enter Account Number: ")
    date_of_birth = input("Enter Date of Birth: ")
    pan_no = input("Enter PAN Number: ")
    email = input("Enter Email ID: ")
    contact_no = input("Enter Contact Number: ")
    address = input("Enter Address: ")
    current_balance = float(input("Enter Balance: "))

    bankDetails = (acc_name, acc_no, date_of_birth, pan_no,
                   [email, contact_no, address, current_balance])

    deposit = float(input("Enter amount to deposit: "))
    bankDetails[4][3] += deposit

    bank_details2.append(bankDetails)
    print("\nAccount created successfully!")
    print(bankDetails)

print("\n-----BANK DETAILS-----")
for acc in bank_details2:
    print(acc) 

while True:
    print("\n1. deposit")
    print("2. withdraw")
    print("3. show account")
    print("4. exit")
    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you!")
        break

    if choice not in (1, 2, 3):
        print("Invalid choice")
        continue

    acc_no = input("Enter account no: ")

    # search the account
    found = None
    for acc in bank_details2:
        if acc[1] == acc_no:
            found = acc
            break

    if found is None:
        print("Account not found!")
        continue

    print("Account found...")

    if choice == 1:
        amount = float(input("Please enter deposit amount: "))
        found[4][3] += amount
        print("Current balance:", found[4][3])

    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        if amount > found[4][3]:
            print("Insufficient balance!")
        else:
            found[4][3] -= amount
        print("Current balance:", found[4][3])

    elif choice == 3:
        print(found)

    print("-----------------------")