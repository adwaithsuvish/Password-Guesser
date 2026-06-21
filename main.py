# START OF THE CODE
#POSSIBLE PASSWORD GENERATOR
import permutation

name = input("Enter your full name: ")
age = input("Enter your age: ")
dob = input("Enter your date of birth (DDMMYYYY): ")
gender = input("Enter your gender (M/F): ")
number_special = input("Enter a special number: ")



special_characters = "~!@#$%^&*()-_=+[]{}|;:',.<>/?" + '"'

passwords = list(permutation.permutation(name.split(), [dob[6:]], list(special_characters)))

print(passwords)
