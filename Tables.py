import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="vmail",passwd="vibhu")
cur1 = mycon.cursor()

def login():
    sql = '''create table login
    (f_name varchar(20) not null,
    l_name varchar(20) not null,
    username varchar(50) not null primary key,
    password varchar(30) not null)'''
    cur1.execute(sql)
    mycon.commit()

def mail():
    sql = '''create table mail
    (receiver varchar(50) not null,
    sender varchar(50) not null,
    message varchar(500) not null,
    subject varchar(50),
    msg_date char(10))'''
    cur1.execute(sql)
    mycon.commit()
    
login()
mail()
cur11.close()
mycon.close()

print("Done")

