print("Welcome to the tip calculator.")
#If the bill was $150.00, split between 5 people, with 12% tip. 
total_bill = float(input("What was the total bill? $"))
# Each person should pay (150.00 / 5) * 1.12 = 33.6
people = int(input("How many people to split the bill? "))
#Format the result to 2 decimal places = 33.60
tip_percentage = int(input("What percentage tip would you like to give?10, 12 or 15? "))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
if tip_percentage == 10:
  amount_to_pay = float((total_bill/people) * 1.1)
  print("Each person should pay: %.2f" %amount_to_pay)
elif tip_percentage == 12:
  amount_to_pay = float((total_bill/people) * 1.12)
  print("Each person should pay: %.2f" %amount_to_pay)
elif tip_percentage == 15:
  amount_to_pay = float((total_bill/people) * 1.15)
  print("Each person should pay: %.2f" %amount_to_pay)
else:
  print("Please enter either 10, 12 or 15")

#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
