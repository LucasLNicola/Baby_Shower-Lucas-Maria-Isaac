https://replit.com/join/byggwccnrp-lucasleite32

sales_people = input("Is there any sales people in your store? ").lower()
print()

salary_b = int(input("How much is the base salary in your store? "))
print()

people_amt = int(input("How many sales people there are in your store? "))

while sales_people == "yes":
  print()
  
  for i in range(people_amt):
    sales_p = input("What's the name of the sales person " + str(i+1) + "?: ")
    print()
    sales_p_amt = int(input(f"How much did the {sales_p} sell in products? "))
    print()
    
    if sales_p_amt < 3500:
      comission = 0.07
      total_s = float(salary_b*(1-comission))
    
    elif sales_p_amt >= 3500 and sales_p_amt <= 7000:
      comission = 0.1
      total_s = float(salary_b*(1-comission))

    elif sales_p_amt > 7000:
      comission = 0.15
      total_s = float(salary_b*(1-comission))

    print()

    print(f"{sales_p} sold {sales_p_amt} products and his/her slarary is {total_s} dollars")
    print()
    
  break
