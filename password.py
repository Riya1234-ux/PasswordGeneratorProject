import random

letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','A','B','O','L','R','S','T','U']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols=['%','$','@','!','^','&']
print("Welcome to Password Generator")
n_letters= int(input("how many letters would u want? "))
n_symbols= int(input("how many symbols would u want? "))
n_numbers= int(input("how many numbers would u want? "))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=''
for char in password_list:
    password+=char
print(password)