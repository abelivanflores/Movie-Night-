import mysql.connector
from mysql.connector import Error
import random
import re



#for my environment, we are using mysql 8.0.21 and an environment using Python 3.6.12 (64-bit)

#the code below will automatically log us in to our database when the program is ran, in a professional environment hard coding credentials are not recommended as they pose a security risk 


#function that creates connection --- Citation: P Lindner, Mainendof3 program
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection


#function that is used to store the results from queries --- Citation: P Lindner, Mainendof3 program
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



# This function executes SQL queries against the database.  --- Citation: P Lindner, Mainendof3 program
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
connection = create_connection("#remote SQL DB", "admin", "admin123", "movienight")





#the following code creates a function that will display our program's main menu, this will be looped to allow our user's to make multiple commands before they quit
def print_menu():
    print ("MAIN MENU")
    print ("****************")       
    print ("a. Add Friend")
    print ("m. Select Friend to Fill Out Movie List")
    print ("u. Select Friend to update Movie List")
    print ("p. Delete Friend from Friend List (Will Also Delete Their Movie List)")
    print ("r. Draw One Random Movie Among Selected Friends")
    print ("q. Exit Program")
    print ("****************\n")

#we set x to 1 as it will be the basis of our while loop    
x = 1  

# main menu code learned from https://stackoverflow.com/questions/32965111/how-do-i-have-python-run-if-statements-based-on-the-users-input
#while loop will be needed for the main menu code below
while x == 1:          ## While loop which will keep going until x = 2
    print('\n')
    print_menu()    ## Displays menu

    
    userInput = input('What would you like to do?\n')




    if userInput == 'a':
        #if the user selects a) to create a friend we will ask for the full name followed by the execution of a command to interact with out database and commiting the changes
        user_first = input("What is their first name?: \n")
        user_last = input("What is their last name?: \n")
        #The code below will run the query to create a new friend
        query = "INSERT INTO friendlist (fname, lname) VALUES ('" + str(user_first) + "','" + str(user_last) + "');"
        execute_query(connection,query)
        print('You have added a friend!\n')






    elif userInput == 'm':
        #if the user selects u) to create a movie list for a friend a contact we will ask for the friend's associated id number to specify which person the movie list belongs to 
        query = "Select * FROM friendlist"
        friendlist = execute_read_query(connection, query)
        print(friendlist)
        #Code below will ask the user to input movies to fill out the selected user's movie list
        friendid = input("What is the 'friendid' number associated with the user? : \n")
        print('Get Ready to Enter 10 Movies!\n')
        m1 = input("Enter your favorite movie: \n")
        m2 = input("Enter your 2nd favorite movie: \n")
        m3 = input("Enter your 3rd favorite movie: \n") 
        m4 = input("Enter your 4th favorite movie: \n")
        m5 = input("Enter your 5th favorite movie: \n")
        m6 = input("Enter your 6th favorite movie: \n")
        m7 = input("Enter your 7th favorite movie: \n")
        m8 = input("Enter your 8th favorite movie: \n")
        m9 = input("Enter your 9th favorite movie: \n")
        m10 = input("Enter your 10th favorite movie: \n")  
        #The code below will run the query to insert the selected movies
        query = ("INSERT INTO movielist (idfriend, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}');".format(friendid,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10))
        execute_query(connection,query)
        print('Movie List Complete!\n')        






    elif userInput == 'p':
        #if the user selects p, we will delete their column from our friendlist table, which will automatically delete their movie list as well, since our database cascades updates.
        query = ("SELECT * FROM friendlist")
        friendlist = execute_read_query(connection, query)
        print(friendlist)   
        #the following code will execute an SQl Command to delete a user from the database
        friendid = input("What is the 'friendid' number associated with the user? : \n")
        query = "DELETE FROM friendlist WHERE idfriend = '" + friendid +"';"
        execute_query(connection,query)







    elif userInput == 'r':
        #if the user selects u) to create a movie list for a friend a contact we will ask for the friend's associated id number to specify which person the movie list belongs to 
        query = ("SELECT * FROM friendlist")
        friendlist = execute_read_query(connection, query)
        print(friendlist)

        idlist = []
        while True:
            friendid = input("Please enter the ID # of each friend, one by one. Enter 'f' to finish : \n")
            if friendid == 'f':
                break
            else:
                idlist.append(friendid)
        randomfriend = random.choice(idlist) #https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

        movieid = random.randint(1,10) #https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

        query = "SELECT movie" + str(movieid) + " FROM movienight.movielist WHERE idfriend = '" + str(randomfriend) +"';"
        chosenmovie = execute_read_query(connection, query)
        #The code below will print out the randomly selected movie from the selected group of friends.
        print(chosenmovie)
        formattedmovie = re.sub('[^A-Za-z0-9]+', ' ', str(chosenmovie))
        print("The chosen movie is '" + formattedmovie +"'")

    elif userInput == 'u':
        #if the user selects u) to create a movie list for a friend a contact we will ask for the friend's associated id number to specify which person the movie list belongs to 
        query = "Select * FROM friendlist"
        friendlist = execute_read_query(connection, query)
        print(friendlist)
        friendid = input("What is the 'friendid' number associated with the user? : \n")
        #Code below will ask the user to input movies to update the selected user's movie list
        print('Get Ready to Enter 10 Movies!\n')
        newm1 = input("Enter your favorite movie: \n")
        newm2 = input("Enter your 2nd favorite movie: \n")
        newm3 = input("Enter your 3rd favorite movie: \n") 
        newm4 = input("Enter your 4th favorite movie: \n")
        newm5 = input("Enter your 5th favorite movie: \n")
        newm6 = input("Enter your 6th favorite movie: \n")
        newm7 = input("Enter your 7th favorite movie: \n")
        newm8 = input("Enter your 8th favorite movie: \n")
        newm9 = input("Enter your 9th favorite movie: \n")
        newm10 = input("Enter your 10th favorite movie: \n")  
        #The code below will run the query to update the selected movies
        query = ("UPDATE movielist SET  movie1 = '{}', movie2 = '{}', movie3 = '{}',movie4 = '{}',movie5 = '{}',movie6 = '{}',movie7 = '{}',movie8 = '{}',movie9 = '{}',movie10 = '{}'  WHERE idfriend = '{}';".format(newm1,newm2,newm3,newm4,newm5,newm6,newm7,newm8,newm9,newm10,friendid))
        execute_query(connection,query)
        print('Movie List Complete!\n')     

    
           
    elif userInput == 'q':
        #this command will quit our program by breaking our while loop and making x = 2, also will print a statement to communicate the termination of the program
        print('Exit Complete, GoodBye!\n')
        #this code will break the loop and thus end the prorgam
        x = 2
        exit

