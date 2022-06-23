# Lancer le projet hello_world

Créer le fichier app.js et y placer le code :

```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Hello_World app listening on port ${port}`)
})
```

Lancer la commande suivante pour lancer le serveur et tester cette première app node  :

```bash
node app.js
```

Cette commande lance le server de dev, ouvre le port 3000 et renvoit en réponse le message 'Hello World!'

Si tout se passe bien on a le message "Hello World app listening on port 3000" qui s'affiche dans le terminal. On peut ouvrir le lien `http://localhost:3000` sur un navigateur et verifier la présence du message 'Hello World!' 
