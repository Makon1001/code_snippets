# Installation

## Node

Download le package :

```bash
curl "https://nodejs.org/dist/latest/node-${VERSION:-$(wget -qO- https://nodejs.org/dist/latest/ | sed -nE 's|.*>node-(.*)\.pkg</a>.*|\1|p')}.pkg" > "$HOME/Downloads/node-latest.pkg" && sudo installer -store -pkg "$HOME/Downloads/node-latest.pkg" -target "/"
```

Avec le gestionnaire de packets brew :

```bash
brew install node
```

## Mise en place d'un projet Express

```bash
mkdir myapp
cd myapp
```

```bash
npm init #initialise le fichier package.json
```

Cette commande demande plusieurs questions :

-> entry point: (index.js) c'est le nom du fichier principale. On lui donner d'autre nom comme aopp.js ou server.js etc...

Puis installer express :

```bash
npm install express
```

-> Commande va telecharger le package express, et init le dossier node_module

Pour une installation temporaire : 

```bash
npm install express --no-save
```

A partir de là, le projet est instancié avec node et express. Il faut maintenant créer le fichier correspondant à l'entry point que l'on a renseigné lors de la commande `npm init`.
