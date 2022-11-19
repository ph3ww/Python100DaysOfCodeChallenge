# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the Ultimate Tip Calculator")

total_bill = input("What was the total bill? ")
total_tip = input("How much tip percentage would you like to give? ")
total_split = input("Split between how many people? ")

final_tip = float(total_tip) / 100  # 12/100 = 0.12
final_bill = float(total_bill) * float(final_tip)  # 150*0.12 = 18
max_bill = float(total_bill) + float(final_bill)  # 150+18 = 168

final_split = float(max_bill) / int(total_split)  # 168 / 5 = 33.6

final_total = round(final_split, 2)
# converts float to string with 2 decimal format
final_total = "{:.2f}".format(final_split)
print(f"Each person should pay ${final_total}")
