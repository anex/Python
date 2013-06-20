import bottle
import pymongo
import sys 
import datetime 
import json 

@bottle.route('/static/:path#.+#', name='static')
def static(path):
    return bottle.static_file(path, root='static')

@bottle.route('/')
@bottle.view('index')
def index():
    return bottle.template('index')

@bottle.route('/registrar')
def registrar():
    return bottle.template('registrar')

@bottle.post('/reg')
def reg():
    sw = 0;

    users = con_mongo('users')

    user = bottle.request.forms.get('user')
    passw = bottle.request.forms.get('pass')

    session = { '_id':user, 'passw':passw}

    try:
        users.insert(session)
        sw = 1;
    except:
        print "insert failed:", sys.exc_info()[0]

    if sw:
        bottle.response.set_cookie("session", user)
        bottle.redirect("/")
    else:
        bottle.redirect("/registrar")


@bottle.route("/list")
def list():
    time = con_mongo('cal')

    date = datetime.datetime.today()

    days = [ 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes' ]   

    n_week = datetime.date(date.year, date.month, date.day).isocalendar()[1]

    f = time.find({'n_week':n_week})

    for s in f:
        try:
            if s["outtime"]:
                try:
                    if lists[s["day"]]:
                        lists[s["day"]] = lists[s["day"]] +" "+ s["user"]
                    else:
                        lists= { s["day"]:s["user"] }
                except:
                    lists= { s["day"]:s["user"] }
        except:
            lists = {'nadie':'nadie'}

    user = bottle.request.get_cookie("session")
    return bottle.template("list.tpl", {'username':user, 'users':lists, 'days':days})

@bottle.route("/ing")
def ing():
    return bottle.template('ing')

@bottle.post('/ingr')
def ingr():
    sw = 0;

    users = con_mongo('users')
    time = con_mongo('cal')

    user = bottle.request.forms.get('user')
    passw = bottle.request.forms.get('pass')

    date = datetime.datetime.today()

    week = { 0:'Lunes',
             1:'Martes',
             2:'Miercoles',
             3:'Jueves',
             4:'Viernes',
           }   

    id_ = "%d" % date.day+"-%d" % date.month+"-%d" % date.year+"-%s" % user 
    intime = "%d" % date.hour+":%d" % date.minute+":%d" % date.second
    in_hour = date.hour
    weekday = week[date.weekday()]
    n_week = datetime.date(date.year, date.month, date.day).isocalendar()[1]

    date = { '_id':id_, 'user':user, 'day':weekday, 'intime':intime, 'in_hour':in_hour, 'n_week':n_week }

    if ( users.find_one({"_id":user, "passw":passw}) ):
        try:
            time.insert(date)
            sw = 1;
        except:
            print "insert failed:", sys.exc_info()[0]

        if sw:
            bottle.response.set_cookie("session", user)
            bottle.redirect("/")
        else:
            return bottle.template("errors", {'typ':'Error al Guardar en DB'})
    else:
        return bottle.template('errors', {'typ':'Nombre de Usuario o Contrasena no validos'})

@bottle.route("/out")
def out():
    return bottle.template('out')

@bottle.post('/outs')
def outs():
    sw = 0;

    users = con_mongo('users')
    time = con_mongo('cal')

    user = bottle.request.forms.get('user')
    passw = bottle.request.forms.get('pass')

    date = datetime.datetime.today()

    week = { 0:'Lunes',
             1:'Martes',
             2:'Miercoles',
             3:'Jueves',
             4:'Viernes',
           }   

    id_ = "%d" % date.day+"-%d" % date.month+"-%d" % date.year+"-%s" % user
    outtime = "%d" % date.hour+":%d" % date.minute+":%d" % date.second
    weekday = week[date.weekday()]


    if ( users.find_one({"_id":user, "passw":passw}) ):

        reg = time.find_one({"_id":id_, "user":user})

        t = date.hour - reg['in_hour']

        if ( (reg) and (t > 4) ):

            reg['outtime'] = outtime

            try:
                time.save(reg)
                sw = 1;
            except:
                print "insert failed:", sys.exc_info()[0]

            if sw:
                bottle.response.set_cookie("session", user)
                bottle.redirect("/")
            else:
                return bottle.template("errors", {'typ':'Error al Guardar en DB'})

        else:
            return bottle.template("errors", {'typ':'Ud no firmo entrada hoy o aun no han pasado al menos 4 horas'})

    else:
        return bottle.template('errors', {'typ':'Nombre de Usuario o Contrasena no validos'})

@bottle.route("/logout")
def logout():
    bottle.response.set_cookie("session", '')
    bottle.redirect("/")

def con_mongo(collection):
    con = pymongo.Connection("mongodb://localhost",   safe=True)

    db = con.asistencia

    if collection == 'users':
        collection = db.users
    elif collection == 'cal':
        collection = db.cal
    else:
        collection = db.users

    return collection

bottle.debug(True)
bottle.run(host='192.168.213.34',  port=8081)
