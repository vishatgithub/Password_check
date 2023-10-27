def pass_check(func):
    def inner(password):
        if password != "Sumeet01":
            print("Incorrect password !!!")
        else:
            func(password)
    return inner
@pass_check
def check(password):
    print("Logged in successfully !")
while True:
    a = input("Enter your password : ")
    check(a)
    if a == "Sumeet01":
        break





