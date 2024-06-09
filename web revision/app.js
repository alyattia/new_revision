// import express
const express = require('express')
// initialize the app (or like router)
const app = express();
// make that as the static folder
const path = require('path');
// get the port from the .env
PORT = process.env.PORT || 8000;
// get the routes
const posts_routes = require('./routes/posts')
// import logger middleware
const logger = require('./middleware/logger')
// use the error handler
const errorHandler = require('./middleware/error')
const notFound = require('./middleware/notFound')
const { fileURLToPath } = require('url')


// body parser (used to be able to handle the body from post requests)
app.use(express.json());
app.use(express.urlencoded({extended: false}));
// set up static folder
app.use(express.static(path.join(__dirname, 'public')))


// define routes
app.use('/posts', logger, posts_routes)

// if you went to a page that doesn't exist have a catch up
app.use(notFound)

// use the error handler (must be below the routes)
app.use(errorHandler);

// sending data
app.get('/bootstrap', (req, res) => {
  // res.send("hello wosrld!");
  res.sendFile(path.join(__dirname, 'bootstrap-proj.html'))
})



// listen to run the server
app.listen(PORT, () => {console.log(`server running at http://localhost:${PORT}/`);});

