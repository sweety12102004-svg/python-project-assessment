units = 350

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

if bill > 3000:
    bill *= 1.10

print("Total Electricity Bill =", bill)

# OUTPUT
Total Electricity Bill = 5775.000000000001
