var express = require('express');
var router = express.Router();

/* GET products page. */
router.get('/', function(req, res, next) {
  res.render('products', { title: "This is the products page", description: "Description products"});
});

module.exports = router;
