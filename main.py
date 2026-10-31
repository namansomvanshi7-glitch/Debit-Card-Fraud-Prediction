# Import Modules
import random
from datetime import datetime

# Card Details
CARD_NUMBER = "1234567890123456"

# Card Verification
print("="*55)
print("        STATE BANK OF INDIA")
print("     DEBIT CARD FRAUD DETECTION")
print("="*55)
import random
from datetime import datetime
print("Debit Card Fraud Detection System")
print("=" * 50)
print("      DEBIT CARD FRAUD DETECTION SYSTEM")
print("=" * 50)

CARD_NUMBER = "1234567890123456"
CVV = "123"
EXPIRY = "12/28"
PIN = "1234"
BALANCE = 100000
print("✅ OTP Verified")
print("🎉 Transaction Successful")

card = input("Enter Your 16-Digit Card Number: ")
if card == CARD_NUMBER:
    print("✅ Card Verified Successfully")

    cvv = input("Enter Your 3-Digit CVV: ")
    if cvv == CVV:
        print("✅ CVV Verified Successfully")

        attempt = 0
        while attempt < 3:
            pin = input("Enter 4-Digit ATM PIN: ")

            if pin == PIN:
               print("✅ PIN Verified")
               break
            else:
                attempt += 1
                print("❌ Wrong PIN")
                print("Remaining Attempts:", 3 - attempt)

if attempt == 3:
    print("🚫 Your Card Has Been Blocked!")
    exit()


    expiry = input("Enter Expiry Date (MM/YY): ")
    if expiry == EXPIRY:
            print("✅ Expiry Date Verified Successfully")

            otp = random.randint(1000, 9999)
            print("Your OTP is:", otp)

            user_otp = int(input("Enter the OTP: "))

            if user_otp == otp:
                print("✅ OTP Verified Successfully")
            else:
                print("❌ Wrong OTP")
                print("⚠️ Fraud Detected!")
                exit()
            print("✅ Expiry Date Verified Successfully")
            print("💳 Transaction Approved!")
            print("✅ otp verified successfully")

            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

choice = int(input("Enter Your Choice: "))
if choice == 1:
    print("\n========== MINI STATEMENT ==========")
    print("Card Number : ************3456")
    print("Available Balance : ₹", BALANCE)
    print("Card Status : ACTIVE")
    print("Last Transaction : Successful")
    print("====================================")

elif choice == 2:
    amount = float(input("Enter Withdraw Amount: ₹"))

    if amount <= BALANCE:
        BALANCE = BALANCE - amount
        print("✅ Withdrawal Successful")
        print("Remaining Balance: ₹", BALANCE)


        transaction_id = random.randint(100000, 999999)
        print("\n========== RECEIPT ==========")
        print("Transaction ID :", transaction_id)
        print("Transaction Successful")
        print("Amount Paid: ₹", amount)
        print("Remaining Balance: ₹", BALANCE)
        print("=============================")
    else:
        print("❌ Insufficient Balance")

elif choice == 3:
    amount = float(input("Enter Deposit Amount: ₹"))
    BALANCE = BALANCE + amount
    print("✅ Deposit Successful")
    print("Updated Balance: ₹", BALANCE)

elif choice == 4:
    print("🙏 Thank You for Using Our ATM")
    exit()

else:
    print("❌ Invalid Choice")


current_time = datetime.now()
amount = float(input("Enter Transaction Amount: ₹"))

if choice == 1:
    print("Your Balance is: ₹", BALANCE)

elif choice == 2:
    amount = float(input("Enter Withdraw Amount: ₹"))

    if amount <= BALANCE:
        BALANCE = BALANCE - amount
        print("✅ Withdrawal Successful")
        print("Remaining Balance: ₹", BALANCE)
    else:
        print("❌ Insufficient Balance")

elif choice == 3:
    amount = float(input("Enter Deposit Amount: ₹"))
    BALANCE = BALANCE + amount
    print("✅ Deposit Successful")
    print("Updated Balance: ₹", BALANCE)

elif choice == 4:
    print("🙏 Thank You for Using Our ATM")
    exit()

print("\nThank you for using our Debit Card Fraud Detection System.")
print("Developed by: Naman Somvanshi")