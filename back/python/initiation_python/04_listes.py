# Liste : types de donner pour stocker des listes comme : pomme poire orange ou chien lapin chat

# Liste sert à enregistrer une collection d'objets, on utilise les [ ]

plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

# Cette liste contient que des chaines de caractères, mais les listes peuvent contenir n'importe quel type de données. 

#  Accéder aux éléments de la liste : 

print(plateformes_sociales[0])
print(plateformes_sociales[1])

# ...

print(plateformes_sociales[-1])

# Accéder au éléments en sens invers en utilisant un index négatif

# Les indices fonctionnent aussi avec les chaines de caractères 

# Une chaine de caractère n'est rien d'autre qu'une liste de caractères : 

langage = "PYTHON"

print(langage[0]) # -> 'P'

# Modifier, retirer, trier une liste : 

# Ajout dans la liste : 

plateformes_sociales.append("Tiktok")
print(plateformes_sociales) # -> ['Facebook', 'Instagram', 'Snapchat', 'Twitter', 'Tiktok']

# Retirer un element : 

plateformes_sociales.remove("Snapchat")
print(plateformes_sociales) # -> ['Facebook', 'Instagram', 'Twitter', 'Tiktok']

# Retire la première instance trouvé dans la liste

#plateformes_sociales.remove("test") # -> ValueError: list.remove(x): x not in list

# La longueur d'une liste : 

longueur_liste = len(plateformes_sociales)

print(longueur_liste) # -> 4

# Tri alphanumérique pour les listes de chaines, et numérique pour les listes de nombres :

plateformes_sociales.sort()
print(plateformes_sociales) # -> ['Facebook', 'Instagram', 'Tiktok', 'Twitter']

# Beaucoup d'autres méthodes existent : https://docs.python.org/fr/3/tutorial/datastructures.html


# Les tuples, sont très similaires aux liste, mais sont immuables, alors que les listes sont modifiables 
# On instancie un tuple avec des ( ) :

mon_tuple = ('donee1', 'donnee2')

# Les dictionnaires : 

# Stocke des paires clés valeurs : 

my_dico = {"rouge": "#FF0000", "vert":"#00FF00", "bleu":"#0000F"}

nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

# On peut aussi initialiser un dictionnaire avec des accolades vides ou avce la fonction dict()

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

# Accéder aux infos du dico : 

print(nouvelle_campagne["responsable_de_campagne"])
print(taux_de_conversion["facebook"])

# Opérations courantes sur les dictionnaires : 

# Ajouter une paire clé valeur : 

infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

# Maintenant return la clé en plus nom_scientifique dans le dico infos_labradoodle

# Pour écraser la valeur poids : 
infos_labradoodle["poids"] ="45 kg"

# Supprimer une paire de clé/valeur :
del infos_labradoodle["origine"]
# ou 
# infos_labradoodle.pop("origine")

# Verifier si une clés existe : 

"poids" in infos_labradoodle # -> True
"race" in infos_labradoodle # -> False