import re

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pwd_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')


def isValidEmail(Username):
    if re.fullmatch(email_regex,Username):
      return True
    else:
      return False

def isValidPwd(Password):
    if len(Password) < 16 and len(Password) > 5 and re.fullmatch(pwd_regex,Password):
      return True
    else:
      return False

def register():
    db = open(r"C:\Users\91809\PycharmProjects\pythonProject3\pythonProject2\logindatabase.txt","r")
    Username = input("Create username:")
    if isValidEmail(Username):
        Password = input("Create password:")
        Password1= input("Confirm password:")
        if isValidPwd(Password):
            d = []
            f = []
            for i in db:
              a,b = i.split(",")
              b = b.strip()
              d.append(a)
              f.append(b)
              data = dict(zip(d, f))
              if Username  in d:
                print("Username exist")
                register()
              elif Password != Password1:
                print("Passwords do not match,restart")
                register()
              elif Password ==Password1:
                print("Valid Password")
              db = open(r"C:\Users\91809\PycharmProjects\pythonProject3\pythonProject2\logindatabase.txt", "a")
              db.write(Username + "," + Password + "\n")
              print("Success!")
              db.close()
              home()
              break
        else:
            print("Invalid Password")
            register()
    else:
        print("Invalid Username")
        register()

def access():
    db = open(r"C:\Users\91809\PycharmProjects\pythonProject3\pythonProject2\logindatabase.txt", "r")
    Username = input("Enter your username:")
    Password = input("Enter your password:")

    if not len(Username or Password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d,f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login success")
                        print("Hi",Username)
                    else:
                        print("Password or Username incorrect")
                except:
                    print("Incorrect password or username")
            else:
                print("Username or Password doesn't exist")
        except:
            print("Useername or password doesn't exist")
    else:
        print("Please enter a value")

def home(option = None):
    option = input("Login|Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
home()



