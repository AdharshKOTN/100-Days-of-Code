import random
print("Welcome to the PyPassword Generator!")
output = ""
char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol_list = "!@#$%^&*_-+=?.,:;()[]"
letter_cnt = int(input("How many letters would you like in your password?\n"))
symbol_cnt = int(input("How many symbols would you like?\n"))
number_cnt = int(input("How many numbers would you like?\n"))

for i in range(0, letter_cnt):
   output += random.choice(char_list)

for i in range(0, number_cnt):
   random_insertion_point = random.randint(0,len(output))
   output = output[:random_insertion_point] + str(random.randint(0,9)) + output[random_insertion_point:]

for i in range(0, symbol_cnt):
   random_insertion_point = random.randint(0,len(output))
   output = output[:random_insertion_point] + str(random.choice(symbol_list)) + output[random_insertion_point:]

print("Here is your password: " + output)
