names = set()

user_input = input("Enter a name: ")
print("new name")
names.add(user_input)
while user_input:
    user_input = input("Enter a name: ")
    if user_input in names:
        print("existing name")
    else:
        print("new name")

    names.add(user_input)
for i in names:
    print(i)





