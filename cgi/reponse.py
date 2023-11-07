import cgi 
import csv

#Lecture du formulaire POST ou GET
form = cgi.FieldStorage()

#Stockage des elements du formulaire dans des variables
nom = form.getvalue("nom")
prenom = form.getvalue("prenom")
mail = form.getvalue("email")
message = form.getvalue("message")

#Enregistre le message dans le fichier
with open('./cgi/messages.csv', 'a',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow((nom,prenom,mail,message))

#envoi le debut de la réponse à la requete
print("Content-type: text/html; charset='utf-8'\n")

#corps de la réponse
html = """<!DOCTYPE html>
<head>
    <title>Reponse</title>
</head>
<body>
	<img src="../images/logo.png" alt="logo" id="logo" />
	<p>Bonjour {} {}, merci pour ton message.</p>
	<p>ton adresse mail est {}.<P>
	<p>ton message est : </p>
	<p>{}</p>
	<a href="../index.html">
    	<button type="submit"> Retour </button>
    <a>
</body>
</html>
""".format(prenom,nom,mail,message)

#envoi le corps de la réponse
print(html)