import random
import string

length = int(input("DIGITE AQUI O TAMANHO DA SENHA ======> "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)

passwrd = "".join(temp)

print(passwrd)