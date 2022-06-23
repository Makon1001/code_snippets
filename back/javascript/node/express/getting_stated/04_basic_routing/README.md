# Init project 

```bash
npm init
 express --git --css --jade
 ```

 # Routing 

Détermine la réponse de l'application à une requête client sur un entry point.

**Exemple** : le client demande `Get` /users, ici l'entry point est `/users`.

L'application va retourner le message : 'respond with a resource'


Les routes sont construite de la manière suivante : 

```javascript
app.METHOD(PATH, HANDLER)
```

- app est une instance d'express.
- METHOD est une methode de requête HTTP, en minuscule
- PATH est une route sur le server
- HANDLER est la fonction exécutée lorsque la route correspond.

**exemple**

```javascript
app.get('/', (req, res) => {
  res.send('Hello World!')
})
```

```javascript
app.post('/', (req, res) => {
  res.send('Got a POST request')
})
```

```javascript
app.put('/user', (req, res) => {
  res.send('Got a PUT request at /user')
})
```

```javascript
app.delete('/user', (req, res) => {
  res.send('Got a DELETE request at /user')
})
```

Dans ce projet, on appel app.Router, il faut donc remplacer app par router. Mais on peut également le faire directement dans le fichier app.js (code moins élégant)

A noter que la base de la route `/users` est set dans app.js, avec : 

```javascript
app.use('/users', usersRouter);
```

C'est une technique valable pour une petite application, mais fait vite grossir le fichier `app.js `sur des applications plus volumineuses.Il est alors préférable d'instancier un index dans le dossier routes, qui va se charger d'appeler ensuite les fichiers de routes correspondantes. Nous aurons donc l'ensemble de la gestion des routes dans le dossier routes, et alège le fichier app.js.