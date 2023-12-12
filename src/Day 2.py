#Commenting
#Day 2:- Data Types, Numbers, Operations, Type Conversion, f-string

# Tip calculator and Bill Splitter

print("Hello, Would you like to pay your bill.")
bill_amount = int(input("What was the total bill? RS."))
tip_percentage = int(input("How much tip you want to pay? 10, 12, 15, 20 "))
split_count = int(input("How many people you wan tto divide this bill? Enter 1 if there is no split. "))

print(f'Total amount to pay is: {bill_amount*(100+tip_percentage)/100}\nAmount to pay per person is: {(bill_amount*(100+tip_percentage)/100)/split_count}')