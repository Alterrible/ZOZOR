import csv

#envoi le debut de la réponse à la requete
print("Content-type: text/html; charset='utf-8'\n")

#debut de la page
html = """<!DOCTYPE html>
<head>
    <title>Liste des Messages</title>
</head>
<body>
	<img src="../images/logo.png" alt="logo" id="logo" />
    <p> Liste des messages reçus : </p>
"""
print(html)

# partie de la page pour chaque message 
with open('./cgi/messages.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        html = """        
        <p>Message de {} {} : </p>
        <p>{}</p>
        """.format(row[1],row[0],row[3]) #format(prenom,nom,message)
        #envoie chaque partie
        print(html)

html = """ 
    <a href="../index.html">
    	<button type="submit"> Retour </button>
    <a>
</body>
</html>
"""
#envoi la fin de la réponse
print(html)





