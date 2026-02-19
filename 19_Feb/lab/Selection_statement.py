amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age (in months): "))
is_international = input("Is the transaction international? (yes/no): ")

if amount > 200000 and account_age < 6 and is_international.lower() == "yes":
    print(" Transaction Flagged for Manual Verification")
else:
    print("Transaction is Normal")

    
