import pandas as pd
import numpy as np
"""
av linus lilja
went into zen mode and just coded without even thinking about what i was typing. Ended up being this in about 20min.
enjoy
"""

x = np.array([1])
y = np.array([4])

class Admin:
    admin = input('Admin alias: ')
    password = '123'
    email = 'admin@adm.in'
class Users(Admin):
    admin = Admin.admin
    username = []
    password = []
    email = []

def main_program():
    df = pd.read_csv('text.csv')
    print(df)
    print(x*y)


def registration():
    print('Vad är ditt alias? ')
    print('_____________')
    Users.username = str(input(''))
    Users.password = str(input('Vad är ditt pw: '))
    Users.email = str(input('Vad är din emailadress?: '))
    print('Tack!')
    logIn(registration=True)

def logIn(registration):
    login_username = input('vad ar ditt alias? : ')
    login_password = input(' Vad är ditt pw ? : ')
    if login_password == Users.password:
        main_program()
    elif login_password != Users.password:
        print('Fel pw. ')
        logIn()
    else:
        pass

registration()
