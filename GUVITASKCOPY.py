import re
#Function for New Registration 
def register():
    Email=input('---------Enter Email ID---------\n')
    regex = '^\w[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    if Email[0].isdigit()== True:
        print('Invalid Email')
        register() 
    elif (re.search(regex,Email)):
        print('Valid Email')
        db=open("dbase.txt","r")
        db=open("dbase.txt","a")
        db.write(Email+'\n')
        print('\n----------Enter Password----------\n')
        print("""Note:Password should contain atleast 
              - one uppercase
              - one lowercase
              - one digit and 
              - one Special character. 
              - Length of the password should be 5 to 16 Characters""")
        passcheck()
    else:
        print('Invalid Email')
        register()
#Function for Password Validation 
def passcheck():
    password=input()
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    pat = re.compile(reg)
    match = re.search(pat,password)
    if match:
        print("Registration Success!")
        db=open("dbase.txt","a")
        db.write(password+" ")
    else:
        print("Invalid Password.Re-Enter Password!")
        passcheck()
#Function to check Login Password 
def pwdcheck():
    pas=input('Enter your Password:')
    if pas in open('dbase.txt').read():
        print('Login Successful')
    else:
        print('Wrong Password!')
        print('Enter 1 - Try again | 2 - Forgot Password')
        opt2=int(input())
        if opt2==1:
            pwdcheck()
        else:
            frgtpass()
#Function for Forgot password
def frgtpass():
    db=open('dbase.txt','r')
    check=input('Enter Registered Email to retrieve Password:')
    c=[]
    d=[]
    for i in db:
        a,b=i.split()
        b=b.strip()
        c.append(b)
        d.append(a)
    data=dict(zip(c,d))
    print('The password for',check,'is',data[check])
#Main Function    
def access():
   
    print(""" Please Enter your option:
          1 : Signup
          2 : Login
          3 : Forgot Password""")   
    option = int(input())
    if option==1:
        register()
    elif option==2:
        user=input("Enter registered Email ID:")
        if user in open('dbase.txt').read():
            print('Username Correct!')
            pwdcheck()
        else:
            print("Username doesn't exist. Continue Registration!")
            register()
    elif option==3:
        frgtpass()
    else:
        print('Enter correct option')
# Calling Main Function    
access()      
            

