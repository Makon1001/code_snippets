# Generer un skeleton d'application : 

Disponible sur les version de node supperieur à 8.2

```bash
npx express-generator # Génère l'arborescence présente dans ce dossier
```

Cette arborescence est une manière d'organiser un projet node express. Mais il en existe d'autres. Utiliser ce qui convient le mieux à votre projet.

Installes les dépendances et lancer le projet :

```bash
npm install
DEBUG=03-express-app-generator:* npm start
```

Pour les version inferieurs :

```bash
npm install -g express-generator
```

```bash
express -h # Pour afficher l'ensemble des commandes disponibles 
```

Exemple : Créer une app Express nommée myapp, qui va créer une arborescence de fichiers et utilise l'engine de view `Pug` avec la commande : 

```bash
 express --view=pug myapp
 ```
