import mysql.connector
from mysql.connector import Error
import random
import re
from flask import Flask, request, jsonify, make_response, abort
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '' # Remote SQL DB
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='admin123'
mysql = MySQL(app)

@app.route('/api/allfriends' ,methods=['GET'])
def allfriends():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM movienight.friendlist''')
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/allmovies', methods=['GET'])
def allmovies():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM movienight.movielist''')
    results = cur.fetchall()
    return jsonify(results)

@app.route('/api/addfriend', methods=['POST'])
def addfriend():
    request_data = request.get_json()
    fname = str(request_data[0]['fname'])
    lname= str(request_data[0]['lname'])
    # now we just have to execute a query in our remote DB
    cur = mysql.connection.cursor()
    query = ("INSERT INTO movienight.friendlist (fname, lname) VALUES (%s,%s);")
    cur.execute(query,(fname,lname))
    mysql.connection.commit()
    return "POST WORKED"


@app.route('/api/addmovies', methods =['GET','POST'])
def addmovies():
    request_data = request.get_json()
    friendid =  request_data[0]['friendid']
    movie1 =  request_data[0]['movie1']
    movie2 =  request_data[0]['movie2']
    movie3 =  request_data[0]['movie3']
    movie4 =  request_data[0]['movie4']
    movie5 =  request_data[0]['movie5']
    movie6 =  request_data[0]['movie6']
    movie7 =  request_data[0]['movie7']
    movie8 =  request_data[0]['movie8']
    movie9 =  request_data[0]['movie9']
    movie10 =  request_data[0]['movie10']
    cur = mysql.connection.cursor()
    query = ("INSERT INTO movienight.movielist (friendid, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}');".format(friendid,movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10))
    cur.execute(query)
    mysql.connection.commit()
    return 'POST WORKED'
    
@app.route('/api/updatemovies', methods =['GET','PUT'])
def updatemovies():
    request_data = request.get_json()
    friendid =  request_data[0]['friendid']
    movie1 =  request_data[0]['movie1']
    movie2 =  request_data[0]['movie2']
    movie3 =  request_data[0]['movie3']
    movie4 =  request_data[0]['movie4']
    movie5 =  request_data[0]['movie5']
    movie6 =  request_data[0]['movie6']
    movie7 =  request_data[0]['movie7']
    movie8 =  request_data[0]['movie8']
    movie9 =  request_data[0]['movie9']
    movie10 =  request_data[0]['movie10']
    cur = mysql.connection.cursor()
    query = ("UPDATE movienight.movielist SET movie1 = '{}',  movie2= '{}', movie3= '{}', movie4= '{}', movie5= '{}', movie6= '{}', movie7= '{}', movie8= '{}', movie9= '{}', movie10= '{}' WHERE friendid = '{}';".format(movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10,friendid))
    cur.execute(query)
    mysql.connection.commit()
    return 'PUT WORKED'


@app.route('/api/removemovies', methods =['DELETE'])
def removemovies():
    request_data = request.get_json()
    friendid =  request_data[0]['friendid']
    cur = mysql.connection.cursor()
    query = ("DELETE FROM movienight.movielist WHERE friendid = '{}';".format(friendid))
    cur.execute(query)
    mysql.connection.commit()
    return 'DELETE WORKED'

@app.route('/api/removefriend?friendselect=<int:friendid>&submit=Submit', methods =['DELETE'])
def removefriend():
    request_data = request.get_json()
    friendid =  request_data
    app.logger.info(request_data)
    cur = mysql.connection.cursor()
    query = ("DELETE FROM movienight.friendlist WHERE friendid = '{}';".format(friendid))
    cur.execute(query)
    app.logger.info(query)
    mysql.connection.commit()
    return 'DELETE WORKED'


@app.route('/api/updatefriend', methods=['PUT'])
def updatefriend():
    request_data = request.get_json()
    friendid =  request_data['friendid']
    fname = str(request_data['fname'])
    lname= str(request_data['lname'])
    # now we just have to execute a query in our remote DB
    cur = mysql.connection.cursor()
    query = ("UPDATE movienight.friendlist SET fname = '{}',lname='{}' WHERE friendid = '{}';")
    cur.execute(query.format(fname,lname,friendid))
    mysql.connection.commit()
    return "PUT WORKED"



@app.route('/api/decision', methods = ['GET','POST'])
def decision():
    cur = mysql.connection.cursor()
    #Input from Frontend
    request_data = request.get_json()
    friendidlist = request_data
    app.logger.info(friendidlist)
    

    




    #API to SQL Server
    

    sqlstring = "SELECT * from movielist WHERE friendid = "

    for item in friendidlist:
        if (item == friendidlist[0]):
            sqlstring = ("SELECT * from movienight.movielist WHERE friendid = '{}'").format(item)
            pass
        else:
            sqlmakervar = " OR friendid = '{}'".format(item)
            sqlstring = sqlstring + sqlmakervar

    query = str(sqlstring + ';')


    app.logger.info(query)


    cur.execute(query)



    results = cur.fetchall()



    fullmovieslist = []
    for row in results:
        fullmovieslist.append(row[2])
        fullmovieslist.append(row[3])
        fullmovieslist.append(row[4])
        fullmovieslist.append(row[5])
        fullmovieslist.append(row[6])
        fullmovieslist.append(row[7])
        fullmovieslist.append(row[8])
        fullmovieslist.append(row[9])
        fullmovieslist.append(row[10])
        fullmovieslist.append(row[11])
            
    #app.logger.info(fullmovieslist)
    indexrange = (len(fullmovieslist)-1)
    randval = random.randrange(0,indexrange)
    randomdecision = fullmovieslist[randval]
    
    return randomdecision
    




if __name__ == '__main__':
    app.run()




