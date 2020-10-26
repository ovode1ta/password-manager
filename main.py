import random
import string
import pyperclip


def pwv():

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=[{]}<,>.'
        password = ''
        for c in range(20):
            password += random.choice(chars)
        mode = input("What would you like to do in the password manager?\noptions: new, list, import\n\n")

        if mode == "list":
            lst = open("passwords.txt", "r")
            print(lst.read() + "\n")
            pwv()

        if mode == "new":
            print("your new password: " + password)
            service = input("What are you using this for?\n")
            username = input("What is the username/email for this service?\n")
            dl = input("Would you like to save this password? (y)es/(n)o\n")
            if dl == "y":
                d = open("passwords.txt", "a")
                d.write(service + " --> " + username + " = " + password + " \n")
                d.close()
                cp = input("Would you like to copy the password to your clipboard?")
                if cp == "y":
                    pyperclip.copy(password)
                else:
                    print("Didn't copy to clipboard.\n")
                    pwv()

                input("Your password has been saved. Press ENTER to continue.")
                pwv()
                
            if dl == "n":
                ocp = input("Would you like to copy the password to your clipboard? y/n\n")
                if ocp == "y":
                    pyperclip.copy(password)
                input("Your password has not been saved. Press enter to close the program")

        if mode == "import":
            iuser = input("What is the username you would like to import?\n")
            ipwd = input("What is the password to this account?\n")
            iser = input("What is this account for?\n")
            f = open("passwords.txt", "a")
            f.write(iser + " --> " + iuser + " = " + ipwd + " \n")
            f.close()
            input("Your password has been successfully imported. Press enter to finish.\n")
            pwv()
        else:
            print("Invalid input. Try again.")
        pwv()

    
pwv()
