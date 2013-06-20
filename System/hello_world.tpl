<!DOCTYPE html>
<html>
<head>
<title>Asitencia Oficina Covetel S/C</title> 
</head>
<body>
<p>
Welcome {{username}} !
</p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<form action="/fruit" method="POST">
What is your favorite fruit?
<input type="text" name="fruit" size="40" value=""><br>
<input type="submit" value="submit">
</form>
</body>
</html>
