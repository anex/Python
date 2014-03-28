import urllib
from xml.dom.minidom import parseString

class Seniat:
    """
    from seniat import Seniat
    r = Seniat()
    
    if r.buscar_rif('V1193389744'):
        print r.nombre
        print r.rif
        print r.agenteRetencionIVA
        print r.contribuyenteIVA
    """
    
    def __init__(self):
        self.rif = '' 
        self.nombre = ''
        self.agenteRetencionIVA = ''
        self.contribuyenteIVA = ''

    def buscar_rif(self,rif=''):
        if rif:
            return self.__buscar(rif)


    def __buscar(self,rif):
        try:
            s = urllib.urlopen("http://contribuyente.seniat.gob.ve/getContribuyente/getrif?rif=%s" % rif)
            xml_data = s.read()
            dom = parseString(xml_data)
            self.rif = rif
            self.nombre = dom.childNodes[0].childNodes[0].firstChild.data 
            self.agenteRetencionIVA = dom.childNodes[0].childNodes[1].firstChild.data 
            self.contribuyenteIVA = dom.childNodes[0].childNodes[2].firstChild.data 
            return True
        except Exception, e:
            self.rif = '' 
            self.nombre = ''
            self.agenteRetencionIVA = ''
            self.contribuyenteIVA = ''
            error = str(e)
            if error.find("Name or service not known") >=0:
                return "sin red"
            else:
                return False
