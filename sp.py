'''
usage: 
import/export data from/to
default destination directory is BASE_DIR/tests/data

import:
dl.py [-h] -i collection.json -d db_name
 
export:
dl.py [-h] -e collection_name -d db_name

default destination directory is BASE_DIR/tests/data
'''

from argparse import ArgumentParser
import argparse, sys
from tools.fixture import Fixture

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='mongodb seeding processor')
    #parser.add_argument('-d', metavar='db_name', nargs='?', help='database name to import/export', required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', metavar='collection_name', nargs='?', help='import collection data from json file')
    group.add_argument('-e', metavar='collection_name', nargs='?', help='export collection to json file')
    
    
    
    args = parser.parse_args()   
    
    fixture = Fixture()
    # db_name set in settings.py
    #db_name = args.d

    # print 'args={0}'.format(vars(args))
    # print 'db_name={0}'.format(db_name)
    if args.i:
        #print 'import collection = {0}'.format(args.i)\
        fixture.load(args.i)
        parser.exit()
    if args.e:
        #print 'export collection = {0}'.format(args.e)
        fixture.dump(args.e)
        parser.exit()
