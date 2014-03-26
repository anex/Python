"""
 Script que imprime en consola reporte en formato org-doc con informacion 
 proveniente de los issues de un repositorio en github y sus comentarios

 Antes de ejecutar el script instalar el modulo PyGithub ejecutando: 
                                                                     
   $ easy_install PyGithub                                               

 Configurar el script asignando valores a las variables:
 
   1. user. (Cuenta github)
   2. password. (Clave cuenta de github)
   3. organizacion. (Organizacion a la que pertenece el repositorio)
   4. repositorio. (Nombre del repositorio)
   5. estado_issues. (Estado de los issues closed/open)

 Para usar el script ejecutar:

   $ python report_github.py > report.org
"""

from github import Github

user = "";
password = ""
organizacion = ""
repositorio = "MPPEE"
estado_issues = ""

g = Github(user, password)

user = g.get_user()

org = g.get_organization(organizacion)

repo = org.get_repo(repositorio)

issues = repo.get_issues(state=estado_issues)

for i in issues:
    datos_responsable = g.get_user(i.assignee.login)
    responsable = datos_responsable.name+" "+datos_responsable.email
    
    fecha = str(i.created_at)
    
    issue = "** "+str(i.number)+": "+i.title+"\n\n*Fecha:* "+fecha+"\n\n*Responsable:* "+responsable+"\n\n*Enlace:* "+i.html_url+"\n\n*** Asunto\n\n"+i.title
    if i.body:
        issue = issue + "\n\n*** Descripcion:\n    #+BEGIN_EXAMPLE\n"+i.body+"\n    #+END_EXAMPLE\n\n"
    else:
        issue = issue + "\n\n*** Descripcion:\n\n No tiene\n\n"
    print issue.encode('utf-8')
    
    comments = i.get_comments()
    
    i = 1

    if comments:
        print "*** Comentarios\n"
    
    for c in comments:
        datos_usuario = g.get_user(c.user.login)
        usuario = datos_responsable.name+" "+datos_responsable.email
        
        fecha = str(c.created_at)
        
        comment = str(i)+". *"+usuario+"* *Fecha:* "+fecha+"\n    #+BEGIN_EXAMPLE\n"+c.body+"\n    #+END_EXAMPLE\n\n"
        print comment.encode('utf-8')
        
        i += 1
