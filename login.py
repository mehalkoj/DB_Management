import datetime
import sqlite3 as lite



conn = lite.connect('vault.db')
cur = conn.cursor()

def initial_db_setup():
    cur.execute(''' CREATE TABLE accounts
    (USERNAME          TEXT      NOT NULL,
    PASSWORD          TEXT      NOT NULL);
    ''')

        



def signup():
    print('********** Please Follow The Prompts Below To Get Your Account Created! **********')

    while 1:
        username = input('Username:  ')
        password = input('Password:  ')
        verpswd = input('Retype Password:  ')

        # data = lite.connect('vault.db').execute("SELECT * FROM accounts").fetchall()

        if verpswd == password:
            
            conn.execute("INSERT INTO accounts VALUES(?, ?);", (username, verpswd))
            conn.commit()
            print('User Account Created!')
            break
        else:
            print('Passwords Dont Match!')



        """ For Debugging
        data=conn.execute('''SELECT * FROM accounts''')
        for row in data:
            print(row)
        conn.commit()"""



def login():
    while 1:
        print('********** Login **********')

        user = input('Username:  ')
        user_query = cur.execute("SELECT EXISTS(SELECT username FROM accounts WHERE username=?)", (user,)).fetchone()

        # Checks the Username and Password to make sure they are valid in DB
        if user_query[0] == 1:
            print ("Name is in table")
            pswd = input('Password:  ')
            pswd_query = cur.execute("SELECT EXISTS(SELECT password FROM accounts WHERE password=?)", (pswd,)).fetchone()
            if pswd_query[0] == 1:
                print('password Correct')
                conn.commit()
                break
            else:
                print('incorrect password')
        else:
            print ("Name is not in table")



while 1:
    print(f'********** Welcome! It Is Currently {datetime.datetime.now()} **********')
    print('1. Login')
    print('2. Sign Up')
    print('3. Reinstall DB')
    print('4. Exit')
    print('************************************************************************')


    x = input('Please Select  ')
    
    if x == '1':
        login()
    elif x == '2':
        signup()
    elif x == '3':
        initial_db_setup()
    elif x == '4':
        conn.close
        break
    else:
        print('Thats not an option')

