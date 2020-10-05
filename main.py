import random
import string

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[{]}|<,>.'
password = ''
for c in range(20):
    password += random.choice(chars)
print("Here is your password:\n" + password)
print('This password takes on average ~300 quintillion years to crack, according to howsecureismypassword.net')
end = input("Press enter to close, reopen for a new password.")

