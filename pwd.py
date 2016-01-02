'''
usage: 
set password for a user

pwd.py [-h] -u user_name -p password_string
'''

from argparse import ArgumentParser
import argparse, sys
from tools.fixture import Fixture

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='password setter')
    parser.add_argument('-u', metavar='username', nargs='?', help='username', required=True)
    parser.add_argument('-p', metavar='password', nargs='?', help='password', required=True)
    
    args = parser.parse_args()   
    
    fixture = Fixture()

    username = args.u
    password = args.p
    
    fixture.set_password(username, password)
    parser.exit()
