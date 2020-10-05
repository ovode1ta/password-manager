import random
import string
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[{]}|<,>.'
password = ''
for c in range(20):
    password += random.choice(chars)
print("Here is your password:\n" + password)
service = input("What are you using this password for? \n")
dl = input("Would you like to download this password? y/n\n")


if dl == "y":
    f = open("passwords.txt", "a")
    f.write(password + " <-- Password for " + service + "\n")
    f.close()
    end = input("Your password has been saved. Press ENTER to finish.")
if dl == "n":
    input("Press enter to close the program")

