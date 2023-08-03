// load the things we need
var express = require('express');
var app = express();

// required module to make calls to a REST API
const axios = require('axios');

// set the view engine to ejs
app.set('view engine', 'ejs');


//parse Jsons with this
const bodyParser = require('body-parser');
const { response } = require('express');
app.use(bodyParser.urlencoded({ extended: true}));
app.use('/public', express.static('public'));

// index page
app.get('/', function(req, res) {
    res.render('pages/index');
});



var friendslist = []

//console.log(friendslist[0].fname)


var friendmovielist = []


var friendchoice = []
var friendvalues = []
var fname = []
var lname = []
var previousfchoice = []


app.all('/addfriend', function(req,res){
  res.render('pages/addfriend')
  var friend = []
  var input = req.body
  console.log(req.body)
  //friend.push(input.addfriendfname)
  //console.log(input.addfriendfname)
  //console.log(input.addfriendlname)
  //friend.push(input.addfriendlname)
  //console.log('2. ' + friend)
  //console.log(friend)


});




var inmovielist = []
var nomovielist = []
var addmoviessearch = []


app.get('/addmovies', function(req,res){


  axios.get('http://127.0.0.1:5000/api/allfriends')
  //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsedfriend = JSON.parse(myjson)
      for(item in parsedfriend){
        format = {'id':parsedfriend[item][0],'fname':parsedfriend[item][1],'lname':parsedfriend[item][2]}
        friendslist.push(format)
        //console.log(format)
      }
        axios.get('http://127.0.0.1:5000/api/allmovies')
                //this makes the response from the api usable
              .then((response2)=>{
                friendmovielist = []
                var fulljson2 = response2.data
                var myjson2 = JSON.stringify(fulljson2)
                parsedmovie = JSON.parse(myjson2)
                for(item in parsedmovie){
                  format = {'id':parsedmovie[item][0],'friendid':parsedmovie[item][1],'movie1':parsedmovie[item][2],'movie2':parsedmovie[item][3],'movie3':parsedmovie[item][4],'movie4':parsedmovie[item][5],'movie5':parsedmovie[item][6],'movie6':parsedmovie[item][7],'movie7':parsedmovie[item][8],'movie8':parsedmovie[item][9],'movie9':parsedmovie[item][10],'movie0':parsedmovie[item][11]}
                  friendmovielist.push(format)
                  //console.log(format)
                }
                
                //console.log(friendmovielist)

                inmovielist = []
                nomovielist = friendslist
                

                
                for(friend in friendslist){

                  for (list in friendmovielist){
                    
                    if (friendslist[friend].id == friendmovielist[list].friendid){
                      inmovielist.push(friendslist[friend])
                    }                  
                  } 
                }
                 
                addmoviessearch = (nomovielist.filter(a => !inmovielist.map(b=>b.id).includes(a.id)))  
                //console.log(addmoviessearch)
                //console.log(friendslist.length)
                //console.log(nomovielist)




                res.render('pages/addmovies',{
                  friendmovielist:friendmovielist,
                  friendslist:friendslist,
                  addmoviessearch
                })
              })
                
              
        



                

      //console.log(friendslist)


      
    
  })

});


/////FINISH LATER
app.post('/addmovies', function(req,res){
  res.render('pages/addmovies',{
    addmoviessearch:addmoviessearch
  })
  
  axios.post('http://127.0.0.1:5000/api/addmovies', {
    
  })

  


});



app.get('/removefriend', function(req,res){
  axios.get('http://127.0.0.1:5000/api/allfriends')
        //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsed = JSON.parse(myjson)
      for(item in parsed){
        format = {'id':parsed[item][0],'fname':parsed[item][1],'lname':parsed[item][2]}
        friendslist.push(format)
      }
        var input = req.body
      //console.log(format)
        friendtodelete = input.friendselect
        //console.log(friendtodelete)



        //console.log(friendslist)


        res.render('pages/removefriend',{
          friendslist:friendslist
        })
        
        //console.log(input)
  })
});

app.all('/removefriend', function(req,res){
  res.render('pages/removefriend',{
        friendslist:friendslist
  })
  var input = req.body
  //console.log(input)
  friendtodelete = input.friendselect
  console.log(friendtodelete)


  axios.delete('http://127.0.0.1:5000/api/removefriend', {
    friendid: friendtodelete

  })
  //console.log(friendtodelete)


});



app.all('/removefriendmovies', function(req,res){
  res.render('pages/removefriendmovies',{
    friendslist:friendslist
  })
  var input = req.body
  //console.log(input)
  friendmovielisttodelete = input.friendselect
  console.log(friendmovielisttodelete)
});




app.all('/allfriends',function(req,res){
  axios.get('http://127.0.0.1:5000/api/allfriends')
        //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsed = JSON.parse(myjson)
      for(item in parsed){
        format = {'id':parsed[item][0],'fname':parsed[item][1],'lname':parsed[item][2]}
        friendslist.push(format)
        //console.log(format)
      }
      
      console.log(friendslist)


      res.render('pages/allfriends',{
        friendmovielist:friendmovielist,
        friendslist:friendslist
      })
          

  })
  
})

app.all('/allfriendmovies',function(req,res){
  axios.get('http://127.0.0.1:5000/api/allmovies')
        //this makes the response from the api usable
    .then((response)=>{
      friendmovielist = []
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsed = JSON.parse(myjson)
      for(item in parsed){
        format = {'id':parsed[item][0],'friendid':parsed[item][1],'movie1':parsed[item][2],'movie2':parsed[item][3],'movie3':parsed[item][4],'movie4':parsed[item][5],'movie5':parsed[item][6],'movie6':parsed[item][7],'movie7':parsed[item][8],'movie8':parsed[item][9],'movie9':parsed[item][10],'movie0':parsed[item][11]}
        friendmovielist.push(format)
        //console.log(format)
      }
      
      console.log(friendmovielist)

      res.render('pages/allfriendmovies',{
        friendmovielist:friendmovielist,
        friendslist:friendslist
      })
  

  })
})









 



app.get('/updatefriendmovies',function(req,res){
  
  res.render('pages/updatefriendmovies',{
    fname:fname,
    lname:lname,
    friendvalues:friendvalues,
    friendchoice:friendchoice


  })
})

var savedid = []

app.all('/updatefriendmovies',function(req,res){
  friendchoice = req.body.friendselect //id of user
  

  for(item in friendmovielist){
    if(friendmovielist[item].friendid == friendchoice){
      friendvalues = friendmovielist[item]
      fname = friendslist[item].fname
      lname = friendslist[item].lname
    }
  }
  


  if (friendchoice==[] || typeof friendchoice == 'undefined'){
    friendchoice= previousfchoice
  }

  
  
  result = req.body
  
  if (result.friendselect !== undefined){
    savedid = req.body
  }

  if (result.friendselect == undefined){
    console.log(savedid)
    result = req.body
    //console.log(result)
    previousfriendid = {friendid: (Number(savedid.friendselect))}
  


    
    //console.log(previousfriendid)
    finalresult = Object.assign({}, previousfriendid, result);
    console.log(finalresult) 

  }
  //console.log(result.friendselect) 
  

  previousfchoice = friendchoice
  //console.log(req.body)

  res.render('pages/updatefriendmovies',{
    fname:fname,
    lname:lname,
    friendvalues:friendvalues,
    friendchoice:friendchoice,
    previousfchoice
  })
})   
   

app.get('/updatefriend', function(req,res){
  axios.get('http://127.0.0.1:5000/api/allfriends')
        //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsed = JSON.parse(myjson)
      for(item in parsed){
        format = {'id':parsed[item][0],'fname':parsed[item][1],'lname':parsed[item][2]}
        friendslist.push(format)
        //console.log(format)
      }
      
      //console.log(friendslist)


      res.render('pages/updatefriend',{
        fname:fname,
        lname:lname,
        friendvalues:friendvalues,
        friendchoice:friendchoice,
        previousfchoice:previousfchoice,
        friendslist:friendslist
      })
          

  })
  var friend = []
});



app.all('/updatefriend', function(req,res){
  axios.get('http://127.0.0.1:5000/api/allfriends')
        //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsed = JSON.parse(myjson)
      for(item in parsed){
        format = {'id':parsed[item][0],'fname':parsed[item][1],'lname':parsed[item][2]}
        friendslist.push(format)
        //console.log(format)
      }
      
      //console.log(friendslist)


      friendchoice = req.body.friendselect //id of user
      console.log(friendchoice)

  for(item in friendslist){
    if(friendslist[item].id == friendchoice){
      fname = friendslist[item].fname
      lname = friendslist[item].lname
    }
  }
      


  if (friendchoice==[] || typeof friendchoice == 'undefined'){
    friendchoice= previousfchoice
  }


  result = req.body

  if (result.friendselect !== undefined){
    savedid = req.body
  }

  if (result.friendselect == undefined){
    //console.log(savedid)
    result = req.body
    //console.log(result)
    previousfriendid = {friendid: (Number(savedid.friendselect))}
  


    
    //console.log(previousfriendid)
    finalresult = Object.assign({}, previousfriendid, result);
    console.log(finalresult)

    axios.put('http://127.0.0.1:5000/api/updatefriend', {
    friendid: finalresult.friendid,
    fname: finalresult.updatefriendfname,
    lname: finalresult.updatefriendlname,

  })
    // .then((response) => {
    //   console.log(response.status);
    //   //render a submission result page
    // }, (error) => {
    //   console.log(error);
    // });

  }
  var friend = []
  var input = req.body


  res.render('pages/updatefriend',{
    fname:fname,
    lname:lname,
    friendvalues:friendvalues,
    friendchoice:friendchoice,
    previousfchoice:previousfchoice,
    friendslist:friendslist
  })
          

  })


  
  

});

 



app.all('/decision',function(req,res){
  console.log(req.body.selected)



  axios.get('http://127.0.0.1:5000/api/allfriends')
  //this makes the response from the api usable
    .then((response)=>{
      friendslist = []
      
      var fulljson = response.data
      var myjson = JSON.stringify(fulljson)
      parsedfriend = JSON.parse(myjson)
      for(item in parsedfriend){
        format = {'friendid':parsedfriend[item][0],'fname':parsedfriend[item][1],'lname':parsedfriend[item][2]}
        friendslist.push(format)
        //console.log(format)
      }
        axios.get('http://127.0.0.1:5000/api/allmovies')
                //this makes the response from the api usable
              .then((response2)=>{
                friendmovielist = []
                var fulljson2 = response2.data
                var myjson2 = JSON.stringify(fulljson2)
                parsedmovie = JSON.parse(myjson2)
                for(item in parsedmovie){
                  format = {'id':parsedmovie[item][0],'friendid':parsedmovie[item][1],'movie1':parsedmovie[item][2],'movie2':parsedmovie[item][3],'movie3':parsedmovie[item][4],'movie4':parsedmovie[item][5],'movie5':parsedmovie[item][6],'movie6':parsedmovie[item][7],'movie7':parsedmovie[item][8],'movie8':parsedmovie[item][9],'movie9':parsedmovie[item][10],'movie0':parsedmovie[item][11]}
                  friendmovielist.push(format)
                  //console.log(format)
                }
                
                //console.log(friendmovielist)
                //console.log(friendslist)
                inmovielist = []
                nomovielist = friendslist
                

                
                for(friend in friendslist){

                  for (list in friendmovielist){
                    
                    if (friendslist[friend].friendid == friendmovielist[list].friendid){
                      inmovielist.push(friendslist[friend])
                    }                  
                  } 
                }
                 
                //addmoviessearch = (nomovielist.filter(a => !inmovielist.map(b=>b.id).includes(a.id)))  
                //console.log(addmoviessearch)
                //console.log(friendslist.length)
                //console.log(inmovielist)




                res.render('pages/decision',{
                  friendmovielist:friendmovielist,
                  friendslist:friendslist,
                  inmovielist: inmovielist
                })
              })
                
             
        



                

      //console.log(friendslist)


      
    
  })
  

});












var server = app.listen()
server.timeout = 600000;

const port = 3000
app.listen(port, () => {
    console.log(`Front-end app listening at http://localhost:${port}`)
});
