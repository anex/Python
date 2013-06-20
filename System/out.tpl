<!DOCTYPE html>
<html>
    <head>
        <title>Asitencia Oficina Covetel S/C - Registro</title> 
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="/static/css/estilo.css" type="text/css" media="screen" chrset="utf8" />
    </head>
    <body>
        <div id ="contenido">
            <div id="title">
                Firmar Salida
            </div>
            <div id="form">
                <form action="/outs" method="POST">
                    <label>Por favor rellene los campos:</label>
                    <label>Usuario:</label>
                    <input type="text" name="user" size="40" value="">
                    <label>Contraseña:</label>
                    <input type="password" name="pass" size="40" value="">
                    <input type="submit" value="Firmar">
                </form>
            </div>
        </div>
    </body>
</html>
