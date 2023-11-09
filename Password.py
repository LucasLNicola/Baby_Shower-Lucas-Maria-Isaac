https://replit.com/@Isaac-JoaquinJo/Passward#main.py

import random

def generate_code():
  length = 8
  password =''.join(random.choices('0123456789', k=length))
  return password 

n_password = generate_code()

print("My new password is", n_password)
