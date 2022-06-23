# Servir des fichiers statiques avec Express

Pour servir des fichiers statics comme des fichiers CSS, Javascript, on utilise la fonction middleware intégrée dans Express : `express.static`

Signature de la fonction :

```javascript
express.static(root, [options])
```

L'argument `root` spécifie le répertoire racine à partir duquel servir les ressources statiques.

**exemple**: Avec ce bout de code on peut maintenat servir les fichier statis qui se trouve dans le répertoire publique

```javascript
app.use(express.static("public"))
```

On peut maintenant charger les ressources suivante :

```http
http://localhost:3000/images/kitchen.jpeg
http://localhost:3000/stylesheets/style.css
http://localhost:3000/javascripts/app-test.js
http://localhost:3000/hello.html
```

Express regarde ce qu'il se trouve dans le répertoire `public`. `public`ne fait pas partie du chemin.

On peut mettre en place plusieurs dossiers de fichier static. Il suffit d'appeler plusieurs fois la fonction middleware express.static.

```javascript
app.use(express.static('public'))
app.use(express.static('files'))
```

Express recherche les fichiers dans l'ordre dans lequel vous avez défini les répertoires statiques avec la fonction middleware `express.static`.

On peut également créer un chemin virtuel :

```javascript
app.use('/static', express.static('public'))
```

Les fichiers seront disponibles aux urls suivantes :

```http
http://localhost:3000/static/images/kitchen.jpeg
http://localhost:3000/static/stylesheets/style.css
http://localhost:3000/static/javascripts/app-test.js
http://localhost:3000//static/hello.html
```

NOTE: For best results, use a reverse proxy cache to improve performance of serving static assets. Un reverse proxy se trouve devant une application Web et effectue des opérations de support sur les requests, en plus de diriger les requests vers l'application. Il peut gérer les pages d'erreur, la compression, la mise en cache, le service des fichiers et l'équilibrage de charge, entre autres.

Le transfert de tâches qui ne nécessitent pas la connaissance de l'état de l'application à un reverse proxy libère Express pour effectuer des tâches d'application spécialisées. Pour cette raison, il est recommandé d'exécuter Express derrière un reverse proxy comme Nginx ou HAProxy en production.


Cependant, le chemin que vous fournissez à la fonction express.static est relatif au répertoire à partir duquel vous lancez votre processus de node. Si vous exécutez l'application express à partir d'un autre répertoire, il est plus sûr d'utiliser le chemin absolu du répertoire que vous souhaitez servir :

```javascript
const path = require('path')
app.use('/static', express.static(path.join(__dirname, 'public')))
```

[Plus d'informations](http://expressjs.com/en/resources/middleware/serve-static.html)

## Lancer le server

```bash
DEBUG=05-static-files:* npm start
```
