const mysql=require('mysql');
const express=require('express');
var app= express();
const bodyparser=require('body-parser');
app.use(bodyparser.json());
//app.use(bodyparser.urlencoded({extended:true}));
const urlencoded = bodyparser.urlencoded({extended:false});
console.log("hello");
app.set("view engine","ejs");
app.set("views","views");

var mysqlConnecttion=mysql.createConnection({
   host:'localhost',
    user:'root',
    password:'MyNewPass',
    database:'pruthiraj',
    insecureAuth:true
});
mysqlConnecttion.connect((err)=>{
   if(!err)
     console.log("connected to database");
   else
       console.log(err);
});
app.listen(3000,()=>console.log("express server is running in3000"));

app.post('/nodebook',urlencoded, (req, res) => {
console.log(req.body);
    var sql="insert into nodestudent values("+req.body.roll+",'"+req.body.name+"','"+req.body.add+"')";
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;

    })
    res.sendFile(__dirname+'/nodebook.html')
});
app.post('/issuebook',urlencoded, (req, res) => {
    console.log(req.body);
    var sql="insert into nodebook values("+req.body.book1+",'"+req.body.name1+"','"+req.body.add1+"')";
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;

    })
    res.sendFile(__dirname+'/issuebook.html')
});
//to issuebook
app.post('/',urlencoded, (req, res) => {
    console.log(req.body);
    var sql="insert into issuebook values("+req.body.book2+","+req.body.roll2+",'"+req.body.insert+"','"+req.body.add2+"')";
    mysqlConnecttion.query(sql,function(err,rows,field) {
        if (err) throw err;
        var sq="delete from nodebook where bookid="+req.body.book2;
        mysqlConnecttion.query(sq,function(err,rows,field) {
            if (err) throw err;
    })

    })

    res.sendFile(__dirname+'/nodebook.html')
    });


app.get('/', function(req,res){
    res.sendFile(__dirname+'/nodestudent.html')
});
app.get('/returnbook', function(req,res){
    res.sendFile(__dirname+'/return book.html')
});
app.get('/issuebook', function(req,res){

    res.sendFile(__dirname+'/issuebook.html')
});
app.get('/allstudent', function(req,res){
    var sql="select * from nodestudent";
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;
        //console.log(rows);
        //var rows=JSON.stringify(rows);
       console.log(rows);

        res.render('allstudent.ejs',{rows: rows});
        //console.log(rows[0].rollno);
    })


});
app.get('/allbook', function(req,res){
    var sql="select * from nodebook";
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;
        console.log(rows);
        //var students=JSON.stringify(rows);

        res.render('allbook.ejs',{rows:rows});
    })

});
//to get a particular student or book data
app.get('/allstudent/:id', function(req,res){
    var sql="select * from nodestudent where rollno=" +req.params.id;
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;
        console.log(rows);
        //var students=JSON.stringify(rows);
        //console.log(students);

        res.render('allstudent.ejs',{rows:rows})
    })


});
app.get('/allbook/:id', function(req,res){
    var sql="select * from nodebook where bookid="+req.params.id;
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;
        console.log(rows);
       // var students=JSON.stringify(rows);

        res.render('allbook.ejs',{rows:rows})
    })

});
//all issuebook
app.get('/allissuebook', function(req,res){
    var sql="select * from issuebook";
    mysqlConnecttion.query(sql,function(err,rows,field)
    {
        if(err) throw err;
        console.log(rows);
       // var students=JSON.stringify(rows);


        res.render('allissuebook.ejs',{students:rows})
    })

});
//to get student stastu
app.get('/allissuebook/:id', function(req,res) {
    var sql = "select * from issuebook where rollno="+req.params.id;
    mysqlConnecttion.query(sql, function (err, rows, field) {
        if (err) throw err;
      //var students = JSON.stringify(rows);
        res.render('allissuebook.ejs', {students: rows})
    })

});
//to return book and add two liabrary
app.post('/sucess',urlencoded, (req, res) => {
    console.log(req.body);
    var sql="insert into nodebook values("+req.body.book3+",'"+req.body.insert2+"','"+req.body.add3+"')";
    mysqlConnecttion.query(sql,function(err,rows,field) {
        if (err) throw err;
        var sq="delete from issuebook where bookid="+req.body.book3;
        mysqlConnecttion.query(sq,function(err,rows,field) {
            if (err) throw err;
        })

    });

    res.render('sucess',{title:"data saved"})
});