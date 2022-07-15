from flask import Flask, render_template, request
from flask_mysqldb import MySQL
#from flask_session import Session
app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'serversiderendering'


@app.route('/')
def index():
    return render_template('home.html')




@app.route('/tables')
def findtablenames():
    cur = mysql.connection.cursor()
    #cur.execute("""SELECT * FROM student_data WHERE id = %s""", (id,))
    cur.execute("""SHOW TABLES""")
    user = cur.fetchone()
    print(user)
    #return render_template('user.html', user = user)
    return user


@app.route('/signup')
def signup():
    return render_template('signup.html')





mysql = MySQL(app)

if __name__ == "__main__":
    app.run()

