<!DOCTYPE html>
<html>
    <head>
        <title>Asitencia Oficina Covetel S/C-list</title> 
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="/static/css/estilo.css" type="text/css" media="screen" chrset="utf8" />
    </head>
    <body>
        <div id ="contenido">
            <div id="title">
                Bienvenido {{username}} !
            </div>
            <table border="1">
                    %for d in days:
                    <tr>
                    <td>{{d}}</td>
                        %try:
                            %if (users[d]):
                                <td>{{users[d]}}</td>
                            %end
                        %except:
                            <td></td>
                        %end
                    </tr>
                     %end
            </table>
            <div id="buttons">
                <span>
                    <a class="buttons" href="/">Volver a inicio</button>
                </span>
                <span>
                    <a class="buttons" href="/logout">Cerrar Sesión</button>
                </span>
            </div>
        </div>
    </body>
</html>
