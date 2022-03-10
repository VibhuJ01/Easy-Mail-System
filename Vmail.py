import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="vmail",passwd="vibhu")
cur1 = mycon.cursor()

def signup():
    global username
    global password
    fname = str(input("Enter your first name\t"))
    sname = str(input("Enter your last name\t"))
    username = str(input("Create your username/email\t"))
    print("Password should have 1 uppercase")
    password = str(input("Create your password\t"))

    print("Validating Username....")
    res = email_validation()

    print("Validating Password....")
    res2 = password_validation()
    if (res == 1 and res2 == 1):
        sql = 'insert into login values(%s,%s,%s,%s)'
        data = (fname,sname,username,password)
        cur1.execute(sql,data)
        mycon.commit()
        print("Signup Complete")

        ch3 = str(input("Do you want to login?(y/n)\t"))
        if(ch3 == 'y' or ch3 == 'Y'):
            login()
        else:
            print("Thank you for using VDmail")
            
    else:
        print("Email or Password is not valid")
        try1 = str(input("Do you want to sign up again?(y/n)"))
        if(try1 == 'y'):
            signup()
        else:
            print("Thank you for using VDmail") 
        
    
        
def email_validation():
    for i in username:
        if(i == '@'):
            print("Username Validation Complete")
            a = 1
            break
    else:
        a = 2
    return a

def password_validation():
    for i in password:
        if(i.isupper() == True):
            print("Password Validation Complete")
            a = 1
            break
    else:
        a = 2
    return a
        
def login():
    global username
    global password
    username = str(input("Enter your username\t"))
    password = str(input("Enter your password\t"))
    
    sql = "select * from login"
    cur1.execute(sql)
    result = cur1.fetchall()
    a = 0
    
    for i in result:
        if(i[2] == username and i[3] == password):
            
            print('Login is succesful')
            ch4 = 'y'
            while(ch4 == 'y'):
                    res = after_login()                   
                    ch4 = str(input("Do you want to continue?(y/n)\t"))
            print("Thank you for using VDmail")

        else:
            continue
    else:
        print("Invalid username or password")
    ch5 = str(input("Do you want to login again?(y/n)\t"))
    if(ch5 == 'y'):
        login()            
    else:
        print("Thank you for using Vmail")
    
def after_login():    
    print("1. Compose")
    print("2. Check Sent ")
    print("3. Inbox")
    print("4. Change Password")

    ch2 = int(input("What do you want to do?\t"))
    if(ch2 == 1):
        res = compose()
        if(res != 1):
            print("That user doesnt exist")
            
    elif(ch2 == 2):
        check_sent()
        
    elif(ch2 == 3):
        inbox()
        
    elif(ch2 == 4):
        change_password()
        
    else:
        print("wrong input")
       
def compose():
    receiver = str(input("Receiver's mail\t"))
    subject = str(input("Enter the subject\t"))
    mail = str(input("Enter your message\t"))
    
    sql = "select * from login"
    cur1.execute(sql)
    result = cur1.fetchall()
    a = 0
    for i in result:
        if(i[2] == receiver):
            sql = 'insert into mail values(%s,%s,%s,%s,%s)'
            data = (receiver,username,mail,subject,ch6)
            cur1.execute(sql,data)
            mycon.commit()
            print("Your message ->",mail,"has been sent") 
            a = 1
        else:
            continue      
    return a

def check_sent():
    sql = "select * from mail"
    cur1.execute(sql)
    result = cur1.fetchall()
    for i in result:
        if(i[1] == username):
            print("Reciever -> ",i[0],"  | Date of mail ->",i[4])
            print("Subject ->",i[3])
            print("Mail ->",i[2])
            print("------------------------------------------------------------------------")
            
def inbox():
    sql = "select * from mail"
    cur1.execute(sql)
    result = cur1.fetchall()
    for i in result:
        if(i[0] == username):
            print("Sender -> ",i[1],"  | Date of mail ->",i[4])
            print("Subject ->",i[3])
            print("Mail ->",i[2])
            print("------------------------------------------------------------------------")
            
def change_password():
    newpass = str(input("Enter new password\t"))
    sql = '''update login 
            set password = %s
            where username = %s'''
    data = (newpass,username)
    cur1.execute(sql,data)
    mycon.commit()
    print("Changing password....")
    print("Your new password is  ",newpass)
   
ch6 = input("Enter today's date(dd/mm/20XX)\t")    
print("1. Signup")
print("2. Login")
ch1 = int(input("what do you want to do?\t"))

if(ch1 == 1):
    signup()
    
elif(ch1 == 2):
    login()
    
else:
    print("wrong input")
cur1.close()
mycon.close()
    

     
