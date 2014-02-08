# *-* coding=utf-8 *-* 
import xmlrpclib, sys, re, pprint

username = "admin"
pwd = "123321..."
dbname = "prueba"
#model = "res.groups"
model = "ir.ui.menu"
attr = ""
value = ""

def connect(username, pwd, dbname):
    # Get the uid
    sock_common = xmlrpclib.ServerProxy ('http://localhost:8069/xmlrpc/common')
    uid = sock_common.login(dbname, username, pwd)

    #replace localhost with the address of the server
    sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
    return sock, uid

def search (sock, uid, dbname, model, filt):
    if filt == "":
        filt = []
    cod = sock.execute(dbname, uid, pwd, model, 'search', filt)
    return cod

def search_detail (sock, uid, dbname, model, attr, value):
    data = []
    fields = []
    if value == "":
        filt = []
    else:
        filt = [(attr,'=', value)]
    cod = search(sock, uid, dbname, model, filt)
    for c in cod:
        detail = sock.execute(dbname, uid, pwd, model, 'read', c, fields)
        data.append(detail)
    return data    

def main():
    (sock, uid) = connect(username, pwd, dbname)
    data = search_detail(sock, uid, dbname, model, attr, value)
    pprint.pprint(data, indent=4)

main()
