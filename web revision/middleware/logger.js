const colors = require('colors')

const logger = (req, res, next) => {
  const methodColors = {
    GET: "green",
    POST: "blue",
    PUT: "yellow",
    DELETE: "red",
  }
  const color = methodColors[req.method] || "white"
  console.log(
    `The middleware runs before ther router function 
    ${req.method} 
    ${req.protocol}:\/\/${req.get('host')}${req.originalUrl}`[
      color
    ]
  );
  next();
}

module.exports = logger;