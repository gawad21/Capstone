// Handles the responses to the http requests sent to landing and login page

const express = require('express');
const router = express.Router();
const { db } = require('../database.js')

const userRef = db.collection('user1').doc('user-info'); //gets reference to a document in the database

/* GET home page (i.e. the landing page). */
router.get('/', function(req, res, next) {
  res.render('landing', { title: 'Landing'});
});

router.get('/login', function(req, res, next) {
  res.render('login', { title: 'Login', invalid: false});
});

router.post('/login', async function(req, res, next) {
  const user_info = await userRef.get(); //reads the JSON document
  let authUser = user_info.data().username;
  let authPass = user_info.data().password;
  var {Username} = req.body;
  var {Password} = req.body;
  //console.log(Username, Password);
  //console.log(authUser, authPass);
  if (Username==authUser && Password==authPass){
    res.redirect('../dashboard'); //redirect to dashboard page
  } else {
    //res.redirect('../'); //brings back to landing page
    res.render('login', { title: 'Login', invalid: true});
  }
  
});

module.exports = router;
