import mysql.connector 
from flask import Flask ,Request, jsonify

app = Flask( __name__ )

db= mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="peopledb"
)
cursor = db.cursor()
 
@app.route('/users',methods=['GET'])
def get_users():
    cursor.execute("select * FROM users")
    return jsonify (cursor.fetchall())


if __name__=='__main__':
    app.run(debug=True)
    
@app.route('/createuser',methods=['post','GET'])
def add_users():
  if(Request.method !='post'):
        return'''<form method="post">
        username:<input type="text" name="name" required><br>
        password:<input type="email" email="email" required><br>
        <input type="submit"value="register">
        </form>
        '''
  else:
      name=Request.form["name"]      
      email=Request.form["email"]
      cursor.execute("INSERT INTO student")