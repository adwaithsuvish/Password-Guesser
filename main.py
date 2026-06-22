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
passwords += list(permutation.permutation(name.split(), list(special_characters), [dob[6:]]))    
passwords += list(permutation.permutation(name.split(),list(special_characters), [dob[0:4]]))    
passwords += list(permutation.permutation(name.split(), list(special_characters), [number_special]))


f = open(f"{name.split()[0]}_passwords.txt", "w")
f.writelines ("\n".join(passwords))
f.close()


print(passwords)
