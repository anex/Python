#!/usr/bin/env python

import pymongo
import sys

def main():
    con = pymongo.Connection("mongodb://localhost",  safe=True)

    db = con.test
    users = db.users

    j = {'firstname':'Carlos', 'lastname':'Paredes'} 

    try:
        users.insert(j)
    except:
        print "insert failed:", sys.exc_info()[0]

    print j

    try:
        users.insert(j)
    except:
        print "insert failed:", sys.exc_info()[0]

main()
