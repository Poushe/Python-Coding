import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
inp_letter=int(input('How many letter you want to add:'))
inp_number=int(input('How many number you want to add:'))
inp_symbols=int(input('How many symbol you want to add:'))

pass_list=[]
for i in range(1,inp_letter+1):
  ran_letter=random.choice(letters)
  pass_list.append(ran_letter)
for j in range(1,inp_number+1):
  pass_list.append(random.choice(numbers))
for k in range(1,inp_symbols+1):
  pass_list.append(random.choice(symbols))
print(pass_list)
random.shuffle(pass_list)
print(pass_list)
strpass=''
for char in pass_list:
  strpass+=char
print(strpass)
  
