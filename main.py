# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print("Your username is {} and domain name is {}".format(username,domain_name))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

