//Handles http requests to the dashboard and other pages
var express = require('express');
var router = express.Router();
const { db } = require('../database.js')

const settingRef = db.collection('user1').doc('settings'); //gets reference to a document in the database
const userRef = db.collection('user1').doc('user-info'); 

/* GET dashboard page. */
router.get('/', function(req, res, next) {
  res.render('dashboard', { title: 'Dashboard'});
});

router.post('/alarm-off-Button-pushed', async function(req, res, next) {
  await settingRef.update({TurnAlarmOFF: true}) ;
  res.status(200).redirect('/dashboard');
});

/* GET settings page. */
router.get('/settings', async function(req, res, next) {
  const user_info = await userRef.get(); 
  var userName = user_info.data().username;
  var passWord = user_info.data().password;
  const settingData = await settingRef.get();
  var {noticeDrowning} = settingData.data();
  var {noticeDistress} = settingData.data();
  var {noticeLeaves} = settingData.data();
  var {alarmEnabled} = settingData.data();
  res.render('settings', {drowning: noticeDrowning, 
                          distress: noticeDistress, 
                          leaves: noticeLeaves, 
                          alarm: alarmEnabled,
                          username: userName,
                          password: passWord
                        });
});

router.post('/settings/:id', async function(req, res, next) {
  let id = req.params.id;
  const settingData = await settingRef.get();
  var {noticeDrowning} = settingData.data();
  var {noticeDistress} = settingData.data();
  var {noticeLeaves} = settingData.data();
  var {alarmEnabled} = settingData.data();
  if(id == 'leaf'){ 
    let current = noticeLeaves;
    await settingRef.update({noticeLeaves: !current}) ;
  }else if(id == 'distress'){
    let current = noticeDistress;
    await settingRef.update({noticeDistress: !current}) ;
  }else if(id == 'drown'){
    let current = noticeDrowning;
    await settingRef.update({noticeDrowning: !current}) ;
  }else if(id == 'alarm'){
    let current = alarmEnabled;
    await settingRef.update({alarmEnabled: !current}) ;
  }
  res.status(200).redirect('/dashboard/settings');
});

module.exports = router;
