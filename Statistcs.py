 https://replit.com/@MariaMartin8/Statistics?s=app

counter2=0
gen_count=0
counter5=0
counter10=0
counter_more10=0
animals_recorded=input("Is there another animal to be recorded?")
while animals_recorded=="yes":
  gen_count+=1
  age=int(input("What is their age?"))
  if age < 2:
    counter2+=1
  elif age >= 2 and age < 5:
    counter5+=1
  elif age >= 5 and age < 10:
    counter10+=1
  elif age >= 10:
    counter_more10+=1
  animals_recorded=input("Is there another animal to be recorded?")
perc2= (counter2/gen_count)*100
perc5=(counter5/gen_count)*100
perc10=(counter10/gen_count)*100
perc_more10=(counter_more10/gen_count)*100
print(f"The total of animals is {gen_count}")
print(f"The total of animals younger than 2 years old is {counter2}")
print(f"The percentage of animals younger than 2 years old is {perc2}")
print(f"The total of animals between 2 and 5 years is {counter5}")
print(f"The percentage of animals between 2 and 5 years is {perc5}")
print(f"The total of animals between 5 and 10 years is {counter10}")
print(f"The percentage of animals between 5 and 10 years is {perc10}")
print(f"The total of animals older than 10 years old is {counter_more10}")
print(f"The percentage of animals older than 10 years old is {perc_more10}")
