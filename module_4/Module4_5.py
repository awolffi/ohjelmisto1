password = "rules"
username = "python"
tries = int(4)

user = input("Enter your username: ")
pas = input("Enter your password: ")

while user != username or pas != password:
    print("something is inncorrect please try again: ")
    user = input("Enter your username: ")
    pas = input("Enter your password: ")
    tries = tries - 1
    if tries == 0:
        break

if user == username and pas == password:
    print("Tervetuloa! ")
else:
    print("Paasy estetty.")


