- Serving static files in Express

```js
app.use(express.static('public'))

// http://localhost:3000/images/kitten.jpg
// http://localhost:3000/css/style.css
// http://localhost:3000/js/app.js
// http://localhost:3000/images/bg.png
// http://localhost:3000/hello.html


```

- serving multiple static files

```js
app.use(express.static('public'))
app.use(express.static('files'))

```

- to create a virtual path as prefix add

```js
app.use("/static", express.static("public"))

// every api should be prefixed with static thing now
```


- dynamic routes


```js
app.get('/users/:userId/books/:bookId', (req, res) => {
  res.send(req.params)
})

```


⚙️ 4. Middleware Basics (req, res, next)


```js
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next(); // move to the next middleware
});

```

🧱 Types of Middleware:

Application-level – Runs on every request (app.use()).

Router-level – Attached to specific routes using express.Router().

Built-in middleware – Like express.json() or express.static().

Third-party middleware – Like cors, helmet, or morgan.

```js
const express = require('express');
const app = express();

const userRoutes = require('./routes/userRoutes');

app.use(express.json());
app.use('/api/users', userRoutes);

module.exports = app;


const app = require('./src/app');

app.listen(3000, () => console.log('Server running on port 3000'));

```

- working with cookies

```js
// app.js
const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();

// Use cookie-parser middleware
app.use(cookieParser());

// Simple route to set a cookie
app.get('/set-cookie', (req, res) => {
  res.cookie('username', 'harshith', { maxAge: 60000 }); // expires in 1 minute
  res.send('Cookie has been set!');
});

// Route to read cookies
app.get('/get-cookie', (req, res) => {
  console.log(req.cookies); // logs: { username: 'harshith' }
  res.send(`Hello ${req.cookies.username}`);
});

// Route to clear cookie
app.get('/clear-cookie', (req, res) => {
  res.clearCookie('username');
  res.send('Cookie cleared!');
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));

```

- creating a signed cookie

```js
app.use(cookieParser('mySecretKey')); // pass a secret key

app.get('/set-signed', (req, res) => {
  res.cookie('token', 'abc123', { signed: true });
  res.send('Signed cookie set!');
});

app.get('/get-signed', (req, res) => {
  console.log(req.signedCookies); // { token: 'abc123' }
  res.send(`Signed cookie value: ${req.signedCookies.token}`);
});

```