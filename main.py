import sqlite3
import pandas as pd

df = pd.read_excel("/Users/shubham/Documents/big data python/userlog/chyper-code.xlsx")
connection = sqlite3.connect("UserDB.db")
cursor = connection.cursor()
# cursor.execute("SELECT * FROM user")
# result = cursor.fetchall()
usertype = df['USER TYPE'].astype(str)
syscon = df['SYSTEM CONVERT'].astype(str)
# print(usertype)
# for r in result:
# print(r)
i = 0
passloop = 0
cc = 0
while i == 0:
    print("************WELCOME*************")
    print("Are you a new user?\n Click Y for Yes\n Click N for NO")
    UD = str(input())
    UD = UD.strip()
    UD = UD.upper()
    if UD == 'Y':
        while cc == 0:
            login = str(input("Enter your email address\t example: firstname.lastname@xyz.com\n"))
            login = login.strip()
            login = login.lower()
            cursor.execute("SELECT * from user where login='" + login + "';")
            usercheck = cursor.fetchall()
            print(usercheck)
            try:
                if usercheck[0][1] == login:
                    print("user already exist try using different username")
                    cc = 0
            except:
                print("Username unique")
                cc = 1
        password = input("Please Enter your Password")
        password = password.upper()
        password.strip()
        up = ''
        for p in password:
            for j in range(0, 36):
                if p == usertype[j]:
                    up += syscon[j]
        result1 = """INSERT INTO user (login,password) VALUES (?,?);"""
        cursor.execute(result1, (login, up))
        connection.commit()
        cursor.close()
        print("*******Account Created Successfully*******\n Thank you for signing up log in to access your account")
        i = int(input("To continue please enter 0\t To exit Enter 1"))
    elif UD == 'N':
        regusercheck = 0
        while regusercheck == 0:
            username1 = input("Please Enter your registered Username\t")
            username1 = username1.lower()
            cursor.execute("SELECT * from user where login='" + username1 + "';")
            results2 = cursor.fetchall()
            #print(results2)
            try:
                if results2[0][1] == username1:
                    # print(results2, "printing value of result2")
                    count = results2[0][3]
                    # print(count, "value of count 3")
                    print("Welcome back", username1)
                    regusercheck = 1
            except:
                print("Uusername does not exist try using different username")
                regusercheck = 0
        while passloop == 0:
            password1 = input("Please Enter your password")
            password1 = password1.upper()
            up2 = ''
            cpass = results2[0][2]
            for p in password1:
                for j in range(0, 36):
                    if p == usertype[j]:
                        up2 += syscon[j]
            # print(up2)
            if up2 == cpass:
                count += 1
                count = str(count)
                cursor.execute("UPDATE user SET count='" + count + "'where login='" + username1 + "';")
                connection.commit()
                cursor.close()
                print("******logged in successful*****\n your login count is", count)
                passloop = 1
                i = 1
            else:
                print("********Password Mismatch*******\n Try again")
                passloop = 0
backupDB = pd.read_sql('SELECT * FROM user', connection)
backupDB.to_csv('userdb-backup.csv', index=False)
