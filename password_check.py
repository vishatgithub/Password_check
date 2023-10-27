def pass_check(func):
    def inner(password,ID):
        if password != "user1234" and ID != "USERID" :
            print("Incorrect password  and ID !!!")
        else:
            func(password,ID)
    return inner
@pass_check
def check(password,ID):
    print("Logged in successfully !")
while True:
    a = input("Enter your password : ")
    b = input("Enter user ID : ")
    check(a,b)
    if a == "user1234" and b == "USERID":
        break





