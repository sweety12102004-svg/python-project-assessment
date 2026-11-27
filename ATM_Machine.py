pin = 1234
entered_pin = 1234
active = True
balance = 30000
amount = 25000

if entered_pin != pin:
    print("Invalid PIN")
elif not active:
    print("Account Inactive")
elif amount <= 0:
    print("Invalid Amount")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif balance - amount < 500:
    print("Minimum balance of 500 required")
else:
    if amount > 20000:
        print("Extra Verification Required")
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)

# OUTPUT
Extra Verification Required
Withdrawal Successful
Remaining Balance = 5000
